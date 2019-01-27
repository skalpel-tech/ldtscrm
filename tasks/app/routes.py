# coding: utf-8
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
"""
    Routes management
    ========================

"""

import urllib
from flask import url_for, current_app
from ._utils import app_context_task


@app_context_task
def show(context):
    app = current_app
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        print(line)
