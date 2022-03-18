#!/usr/bin/env python3

class Config:
    """Flask configuration variables.
    """

    # General Config
    FLASK_APP = "wsgi.py"
    FLASK_ENV = "production"

    # Assets
    LESS_BIN = "/usr/local/bin/lessc"
    ASSETS_DEBUG = "False"
    LESS_RUN_IN_DEBUG = "False"

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    COMPRESSOR_DEBUG ="True"
