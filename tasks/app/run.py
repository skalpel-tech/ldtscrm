# encoding: utf-8
# pylint: disable=too-many-arguments
"""
Application execution related tasks for Invoke.
"""
import os

from invoke import task

@task(
    default=True,
    help={
        'host': "server host name, default:127.0.0.1",
        'port': "server port, default:8888",
        'flask-config': "flask config: [development,testing,production,local]"
    })
def run(
    context,
    host='127.0.0.1',
    port=8888,
    flask_config=None
    ):
    #pylint: disable=unused-argument
    """
    Run LTDS CRM RESTful API Server
    """
    if flask_config is not None:
        os.environ['FLASK_CONFIG'] = flask_config

    from app import create_app
    app = create_app()

    use_reloader = app.debug

    return app.run(host=host, port=port, use_reloader=use_reloader)
