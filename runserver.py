#!/usr/bin/env python

import os

import argparse

from example import create_app

from werkzeug.serving import run_simple

if __name__ == '__main__':

    app = create_app()

    args = {
        'application'   : app,
        'hostname'      : '0.0.0.0',
        'port'          : 8888,
        'use_reloader'  : True,
        'use_debugger'  : True,
        #'ssl_context'   : 'adhoc',
        #'threaded'      : True
    }

    run_simple(**args)
