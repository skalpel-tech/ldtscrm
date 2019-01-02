import os
import platform
import sys

from invoke import Collection, task, run
from invoke.executor import Executor

from . import app

namespace = Collection(
    app
)

def invoke_execute(context, command_name, **kwargs):
    """
    Helper function to make invoke-tasks execution easier.
    """
    results = Executor(namespace, config=context.config).execute((command_name, kwargs))
    target_task = context.root_namespace[command_name]
    return results[target_task]

namespace.configure({
    'run': {
        'shell': '/bin/sh' if platform.system() != 'Windows' else os.environ.get('COMSPEC'),
    },
    'root_namespace': namespace,
    'invoke_execute': invoke_execute,
})
