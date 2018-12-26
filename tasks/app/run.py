# encoding: utf-8
# pylint: disable=too-many-arguments
"""
Application execution related tasks for Invoke.
"""

from invoke import task

@task(default=True)
def run(c):
    """
    Run LTDS CRM RESTful API Server
    """

    from src.app import create_app
    from src.app.config import settings

    app = create_app()
    return app.run(debug=settings.FLASK_DEBUG)