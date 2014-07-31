export GALAXY_SLOTS_CONFIGURED="1"
if [ -n "$SLURM_NTASKS" ]; then
    # May want to multiply this by ${SLURM_CPUS_PER_TASK:-1}.
    # SLURM_NTASKS is total tasks over all nodes so this is 
    # shouldn't be used for multi-node requests.
    GALAXY_SLOTS="$SLURM_NTASKS"
elif [ -n "$NSLOTS" ]; then
    GALAXY_SLOTS="$NSLOTS"
elif [ -f "$PBS_NODEFILE" ]; then
    GALAXY_SLOTS=`wc -l < $PBS_NODEFILE`
else
    GALAXY_SLOTS="1"
    unset GALAXY_SLOTS_CONFIGURED
fi
