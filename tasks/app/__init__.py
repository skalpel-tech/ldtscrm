# encoding: utf-8
"""
Application related tasks for Invoke.
"""

from invoke import Collection

from . import run, db, routes

namespace = Collection(
    run,
    db,
    routes,
)
