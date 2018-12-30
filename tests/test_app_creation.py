# encoding: utf-8
# pylint: disable=missing-docstring
import pytest

from app import create_app


def test_create_app():
    try:
        create_app()
    except SystemExit:
        # Clean git repository doesn't have `local_config.py`, so it is fine
        # if we get SystemExit error.
        pass
