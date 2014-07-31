"""
Job runner plugin for executing jobs on the local system via the command line.
"""
import os
import errno
import logging
import datetime
import tempfile
import subprocess

from time import sleep

from galaxy import model
from galaxy.jobs.runners import BaseJobRunner
from galaxy.util import DATABASE_MAX_STRING_SIZE, shrink_stream_by_size

log = logging.getLogger( __name__ )

__all__ = [ 'LocalJobRunner' ]


class LocalJobRunner( BaseJobRunner ):
    """
    Job runner backed by a finite pool of worker threads. FIFO scheduling
    """
    runner_name = "LocalRunner"

    def __init__( self, app, nworkers ):
        """Start the job runner """

        #create a local copy of os.environ to use as env for subprocess.Popen
        self._environ = os.environ.copy()

        # put lib into the PYTHONPATH for subprocesses
        if 'PYTHONPATH' in self._environ:
            self._environ['PYTHONPATH'] = '%s:%s' % ( self._environ['PYTHONPATH'], os.path.abspath( 'lib' ) )
        else:
            self._environ['PYTHONPATH'] = os.path.abspath( 'lib' )

        #Set TEMP if a valid temp value is not already set
        if not ( 'TMPDIR' in self._environ or 'TEMP' in self._environ or 'TMP' in self._environ ):
            self._environ[ 'TEMP' ] = tempfile.gettempdir()

        super( LocalJobRunner, self ).__init__( app, nworkers )
        self._init_worker_threads()

    def __command_line( self, job_wrapper ):
        """
        """
        command_line = job_wrapper.runner_command_line

        ## slots would be cleaner name, but don't want deployers to see examples and think it
        ## is going to work with other job runners.
        slots = job_wrapper.job_destination.params.get( "local_slots", None )
        command_line = command_line.lstrip( " ;" )
        if slots:
            command_line = 'GALAXY_SLOTS="%d"; export GALAXY_SLOTS; GALAXY_SLOTS_CONFIGURED="1"; export GALAXY_SLOTS_CONFIGURED; %s' % ( int( slots ), command_line )
        else:
            command_line = 'GALAXY_SLOTS="1"; export GALAXY_SLOTS; %s' % command_line
        return command_line

    def queue_job( self, job_wrapper ):
        # prepare the job
        if not self.prepare_job( job_wrapper ):
            return

        stderr = stdout = ''
        exit_code = 0

        # command line has been added to the wrapper by prepare_job()
        command_line = self.__command_line( job_wrapper )

        job_id = job_wrapper.get_id_tag()

        try:
            log.debug( '(%s) executing: %s' % ( job_id, command_line ) )
            stdout_file = tempfile.NamedTemporaryFile( suffix='_stdout', dir=job_wrapper.working_directory )
            stderr_file = tempfile.NamedTemporaryFile( suffix='_stderr', dir=job_wrapper.working_directory )
            proc = subprocess.Popen( args=command_line,
                                     shell=True,
                                     cwd=job_wrapper.working_directory,
                                     stdout=stdout_file,
                                     stderr=stderr_file,
                                     env=self._environ,
                                     preexec_fn=os.setpgrp )
            job_wrapper.set_job_destination(job_wrapper.job_destination, proc.pid)
            job_wrapper.change_state( model.Job.states.RUNNING )
            job_start = datetime.datetime.now()
            i = 0
            # Iterate until the process exits, periodically checking its limits
            while proc.poll() is None:
                i += 1
                if (i % 20) == 0:
                    msg = job_wrapper.check_limits(runtime=datetime.datetime.now() - job_start)
                    if msg is not None:
                        job_wrapper.fail(msg)
                        log.debug('(%s) Terminating process group' % job_id)
                        self._terminate(proc)
                        return
                else:
                    sleep(1)
            # Reap the process and get the exit code.
            exit_code = proc.wait()
            stdout_file.seek( 0 )
            stderr_file.seek( 0 )
            stdout = shrink_stream_by_size( stdout_file, DATABASE_MAX_STRING_SIZE, join_by="\n..\n", left_larger=True, beginning_on_size_error=True )
            stderr = shrink_stream_by_size( stderr_file, DATABASE_MAX_STRING_SIZE, join_by="\n..\n", left_larger=True, beginning_on_size_error=True )
            stdout_file.close()
            stderr_file.close()
            log.debug('execution finished: %s' % command_line)
        except Exception:
            job_wrapper.fail( "failure running job", exception=True )
            log.exception("failure running job %d" % job_wrapper.job_id)
            return
        self._handle_metadata_externally( job_wrapper, resolve_requirements=True )
        # Finish the job!
        try:
            job_wrapper.finish( stdout, stderr, exit_code )
        except:
            log.exception("Job wrapper finish method failed")
            job_wrapper.fail("Unable to finish job", exception=True)

    def stop_job( self, job ):
        #if our local job has JobExternalOutputMetadata associated, then our primary job has to have already finished
        job_ext_output_metadata = job.get_external_output_metadata()
        if job_ext_output_metadata:
            pid = job_ext_output_metadata[0].job_runner_external_pid  # every JobExternalOutputMetadata has a pid set, we just need to take from one of them
        else:
            pid = job.get_job_runner_external_id()
        if pid in [ None, '' ]:
            log.warning( "stop_job(): %s: no PID in database for job, unable to stop" % job.get_id() )
            return
        pid = int( pid )
        if not self._check_pid( pid ):
            log.warning( "stop_job(): %s: PID %d was already dead or can't be signaled" % ( job.get_id(), pid ) )
            return
        for sig in [ 15, 9 ]:
            try:
                os.killpg( pid, sig )
            except OSError, e:
                log.warning( "stop_job(): %s: Got errno %s when attempting to signal %d to PID %d: %s" % ( job.get_id(), errno.errorcode[e.errno], sig, pid, e.strerror ) )
                return  # give up
            sleep( 2 )
            if not self._check_pid( pid ):
                log.debug( "stop_job(): %s: PID %d successfully killed with signal %d" % ( job.get_id(), pid, sig ) )
                return
        else:
            log.warning( "stop_job(): %s: PID %d refuses to die after signaling TERM/KILL" % ( job.get_id(), pid ) )

    def recover( self, job, job_wrapper ):
        # local jobs can't be recovered
        job_wrapper.change_state( model.Job.states.ERROR, info="This job was killed when Galaxy was restarted.  Please retry the job." )

    def _check_pid( self, pid ):
        try:
            os.kill( pid, 0 )
            return True
        except OSError, e:
            if e.errno == errno.ESRCH:
                log.debug( "_check_pid(): PID %d is dead" % pid )
            else:
                log.warning( "_check_pid(): Got errno %s when attempting to check PID %d: %s" % ( errno.errorcode[e.errno], pid, e.strerror ) )
            return False

    def _terminate( self, proc ):
        os.killpg( proc.pid, 15 )
        sleep( 1 )
        if proc.poll() is None:
            os.killpg( proc.pid, 9 )
        return proc.wait()  # reap
