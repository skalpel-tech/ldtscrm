from invoke import Collection, task, run

from . import app

namespace = Collection(
    app
)
