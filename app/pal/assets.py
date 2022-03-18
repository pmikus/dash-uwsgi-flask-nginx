"""Compile static assets.
"""

from flask import current_app as app
from flask_assets import Bundle


def compile_static_assets(assets):
    """Compile stylesheets if in development mode.

    :param assets: Flask-Assets Environment.
    :type assets: Environment
    :returns: Compiled stylesheets.
    :rtype: Environment
    """

    assets.auto_build = True
    assets.debug = False
    less_bundle = Bundle(
        u"less/*.less",
        filters=u"less,cssmin",
        output=u"dist/css/styles.css",
        extra={u"rel": u"stylesheet/less"},
    )
    assets.register(u"less_all", less_bundle)
    if app.config[u"FLASK_ENV"] == u"development":
        less_bundle.build()

    return assets
