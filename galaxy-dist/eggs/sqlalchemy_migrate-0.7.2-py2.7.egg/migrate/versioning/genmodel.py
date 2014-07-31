"""
Code to generate a Python model from a database or differences
between a model and database.

Some of this is borrowed heavily from the AutoCode project at:
http://code.google.com/p/sqlautocode/
"""

import sys
import logging

import sqlalchemy

import migrate
import migrate.changeset


log = logging.getLogger(__name__)
HEADER = """
## File autogenerated by genmodel.py

from sqlalchemy import *
meta = MetaData()
"""

DECLARATIVE_HEADER = """
## File autogenerated by genmodel.py

from sqlalchemy import *
from sqlalchemy.ext import declarative

Base = declarative.declarative_base()
"""


class ModelGenerator(object):
    """Various transformations from an A, B diff.

    In the implementation, A tends to be called the model and B
    the database (although this is not true of all diffs).
    The diff is directionless, but transformations apply the diff
    in a particular direction, described in the method name.
    """

    def __init__(self, diff, engine, declarative=False):
        self.diff = diff
        self.engine = engine
        self.declarative = declarative

    def column_repr(self, col):
        kwarg = []
        if col.key != col.name:
            kwarg.append('key')
        if col.primary_key:
            col.primary_key = True  # otherwise it dumps it as 1
            kwarg.append('primary_key')
        if not col.nullable:
            kwarg.append('nullable')
        if col.onupdate:
            kwarg.append('onupdate')
        if col.default:
            if col.primary_key:
                # I found that PostgreSQL automatically creates a
                # default value for the sequence, but let's not show
                # that.
                pass
            else:
                kwarg.append('default')
        args = ['%s=%r' % (k, getattr(col, k)) for k in kwarg]

        # crs: not sure if this is good idea, but it gets rid of extra
        # u''
        name = col.name.encode('utf8')

        type_ = col.type
        for cls in col.type.__class__.__mro__:
            if cls.__module__ == 'sqlalchemy.types' and \
                not cls.__name__.isupper():
                if cls is not type_.__class__:
                    type_ = cls()
                break

        type_repr = repr(type_)
        if type_repr.endswith('()'):
            type_repr = type_repr[:-2]

        constraints = [repr(cn) for cn in col.constraints]

        data = {
            'name': name,
            'commonStuff': ', '.join([type_repr] + constraints + args),
        }

        if self.declarative:
            return """%(name)s = Column(%(commonStuff)s)""" % data
        else:
            return """Column(%(name)r, %(commonStuff)s)""" % data

    def _getTableDefn(self, table, metaName='meta'):
        out = []
        tableName = table.name
        if self.declarative:
            out.append("class %(table)s(Base):" % {'table': tableName})
            out.append("    __tablename__ = '%(table)s'\n" %
                            {'table': tableName})
            for col in table.columns:
                out.append("    %s" % self.column_repr(col))
            out.append('\n')
        else:
            out.append("%(table)s = Table('%(table)s', %(meta)s," %
                       {'table': tableName, 'meta': metaName})
            for col in table.columns:
                out.append("    %s," % self.column_repr(col))
            out.append(")\n")
        return out

    def _get_tables(self,missingA=False,missingB=False,modified=False):
        to_process = []
        for bool_,names,metadata in (
            (missingA,self.diff.tables_missing_from_A,self.diff.metadataB),
            (missingB,self.diff.tables_missing_from_B,self.diff.metadataA),
            (modified,self.diff.tables_different,self.diff.metadataA),
                ):
            if bool_:
                for name in names:
                    yield metadata.tables.get(name)

    def genBDefinition(self):
        """Generates the source code for a definition of B.

        Assumes a diff where A is empty.

        Was: toPython. Assume database (B) is current and model (A) is empty.
        """

        out = []
        if self.declarative:
            out.append(DECLARATIVE_HEADER)
        else:
            out.append(HEADER)
        out.append("")
        for table in self._get_tables(missingA=True):
            out.extend(self._getTableDefn(table))
        return '\n'.join(out)

    def genB2AMigration(self, indent='    '):
        '''Generate a migration from B to A.

        Was: toUpgradeDowngradePython
        Assume model (A) is most current and database (B) is out-of-date.
        '''

        decls = ['from migrate.changeset import schema',
                 'pre_meta = MetaData()',
                 'post_meta = MetaData()',
                ]
        upgradeCommands = ['pre_meta.bind = migrate_engine',
                           'post_meta.bind = migrate_engine']
        downgradeCommands = list(upgradeCommands)

        for tn in self.diff.tables_missing_from_A:
            pre_table = self.diff.metadataB.tables[tn]
            decls.extend(self._getTableDefn(pre_table, metaName='pre_meta'))
            upgradeCommands.append(
                "pre_meta.tables[%(table)r].drop()" % {'table': tn})
            downgradeCommands.append(
                "pre_meta.tables[%(table)r].create()" % {'table': tn})

        for tn in self.diff.tables_missing_from_B:
            post_table = self.diff.metadataA.tables[tn]
            decls.extend(self._getTableDefn(post_table, metaName='post_meta'))
            upgradeCommands.append(
                "post_meta.tables[%(table)r].create()" % {'table': tn})
            downgradeCommands.append(
                "post_meta.tables[%(table)r].drop()" % {'table': tn})

        for (tn, td) in self.diff.tables_different.iteritems():
            if td.columns_missing_from_A or td.columns_different:
                pre_table = self.diff.metadataB.tables[tn]
                decls.extend(self._getTableDefn(
                    pre_table, metaName='pre_meta'))
            if td.columns_missing_from_B or td.columns_different:
                post_table = self.diff.metadataA.tables[tn]
                decls.extend(self._getTableDefn(
                    post_table, metaName='post_meta'))

            for col in td.columns_missing_from_A:
                upgradeCommands.append(
                    'pre_meta.tables[%r].columns[%r].drop()' % (tn, col))
                downgradeCommands.append(
                    'pre_meta.tables[%r].columns[%r].create()' % (tn, col))
            for col in td.columns_missing_from_B:
                upgradeCommands.append(
                    'post_meta.tables[%r].columns[%r].create()' % (tn, col))
                downgradeCommands.append(
                    'post_meta.tables[%r].columns[%r].drop()' % (tn, col))
            for modelCol, databaseCol, modelDecl, databaseDecl in td.columns_different:
                upgradeCommands.append(
                    'assert False, "Can\'t alter columns: %s:%s=>%s"' % (
                    tn, modelCol.name, databaseCol.name))
                downgradeCommands.append(
                    'assert False, "Can\'t alter columns: %s:%s=>%s"' % (
                    tn, modelCol.name, databaseCol.name))

        return (
            '\n'.join(decls),
            '\n'.join('%s%s' % (indent, line) for line in upgradeCommands),
            '\n'.join('%s%s' % (indent, line) for line in downgradeCommands))

    def _db_can_handle_this_change(self,td):
        """Check if the database can handle going from B to A."""

        if (td.columns_missing_from_B
            and not td.columns_missing_from_A
            and not td.columns_different):
            # Even sqlite can handle column additions.
            return True
        else:
            return not self.engine.url.drivername.startswith('sqlite')

    def runB2A(self):
        """Goes from B to A.

        Was: applyModel. Apply model (A) to current database (B).
        """

        meta = sqlalchemy.MetaData(self.engine)

        for table in self._get_tables(missingA=True):
            table = table.tometadata(meta)
            table.drop()
        for table in self._get_tables(missingB=True):
            table = table.tometadata(meta)
            table.create()
        for modelTable in self._get_tables(modified=True):
            tableName = modelTable.name
            modelTable = modelTable.tometadata(meta)
            dbTable = self.diff.metadataB.tables[tableName]

            td = self.diff.tables_different[tableName]

            if self._db_can_handle_this_change(td):

                for col in td.columns_missing_from_B:
                    modelTable.columns[col].create()
                for col in td.columns_missing_from_A:
                    dbTable.columns[col].drop()
                # XXX handle column changes here.
            else:
                # Sqlite doesn't support drop column, so you have to
                # do more: create temp table, copy data to it, drop
                # old table, create new table, copy data back.
                #
                # I wonder if this is guaranteed to be unique?
                tempName = '_temp_%s' % modelTable.name

                def getCopyStatement():
                    preparer = self.engine.dialect.preparer
                    commonCols = []
                    for modelCol in modelTable.columns:
                        if modelCol.name in dbTable.columns:
                            commonCols.append(modelCol.name)
                    commonColsStr = ', '.join(commonCols)
                    return 'INSERT INTO %s (%s) SELECT %s FROM %s' % \
                        (tableName, commonColsStr, commonColsStr, tempName)

                # Move the data in one transaction, so that we don't
                # leave the database in a nasty state.
                connection = self.engine.connect()
                trans = connection.begin()
                try:
                    connection.execute(
                        'CREATE TEMPORARY TABLE %s as SELECT * from %s' % \
                            (tempName, modelTable.name))
                    # make sure the drop takes place inside our
                    # transaction with the bind parameter
                    modelTable.drop(bind=connection)
                    modelTable.create(bind=connection)
                    connection.execute(getCopyStatement())
                    connection.execute('DROP TABLE %s' % tempName)
                    trans.commit()
                except:
                    trans.rollback()
                    raise
