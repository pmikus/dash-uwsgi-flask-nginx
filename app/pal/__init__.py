"""Initialize Flask app.
"""

import logging

from flask import Flask
from flask_assets import Environment


def init_app():
    """Construct core Flask application with embedded Dash app.
    """

    logging.basicConfig(
        format=u"%(asctime)s: %(levelname)s: %(message)s",
        datefmt=u"%Y/%m/%d %H:%M:%S",
        level=logging.INFO
    )

    logging.info("Application started.")

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(u"config.Config")

    with app.app_context():
        # Import parts of our core Flask app.
        from . import routes
        from .assets import compile_static_assets

        assets = Environment()
        assets.init_app(app)

        # Compile static assets.
        compile_static_assets(assets)

        # Import Dash applications.
        from .report.report import init_report
        app = init_report(app)

    return app

app = init_app()
