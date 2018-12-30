# encoding: utf-8
# pylint: disable=too-many-arguments
"""
Application execution related tasks for Invoke.
"""

from invoke import task

@task(default=True)
def run():
    """
    Run LTDS CRM RESTful API Server
    """

    from app import create_app
    from app.config import settings

    app = create_app()
    return app.run(debug=settings.FLASK_DEBUG)
