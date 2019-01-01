# encoding: utf-8
"""
Flask-SQLAlchemy adapter
------------------------
"""
import sqlite3

from sqlalchemy import engine, MetaData

from .flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy

class SQLAlchemy(BaseSQLAlchemy):
    """
    Customized Flask-SQLAlchemy adapter with enabled autocommit, constraints
    auto-naming conventions and ForeignKey constraints for SQLite.
    """

    def __init__(self, *args, **kwargs):
        if 'session_options' not in kwargs:
            kwargs['session_options'] = {}
        kwargs['session_options']['autocommit'] = True
        # Configure Constraint Naming Conventions:
        # http://docs.sqlalchemy.org/en/latest/core/constraints.html#constraint-naming-conventions
        kwargs['metadata'] = MetaData(
            naming_convention={
                'pk': 'pk_%(table_name)s',
                'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
                'ix': 'ix_%(table_name)s_%(column_0_name)s',
                'uq': 'uq_%(table_name)s_%(column_0_name)s',
                'ck': 'ck_%(table_name)s_%(constraint_name)s',
            }
        )
        super(SQLAlchemy, self).__init__(*args, **kwargs)

    def init_app(self, app):
        super(SQLAlchemy, self).init_app(app)

        database_uri = app.config['SQLALCHEMY_DATABASE_URI']
        assert database_uri, "SQLALCHEMY_DATABASE_URI must be configured!"
