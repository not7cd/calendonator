import os
from flask import Flask
from flask_common import Common

app = Flask(__name__)
common = Common(app)

# TODO: better config
app.config.from_object("calendonator.default_settings")
app.config.from_envvar("CALENDONATOR_SETTINGS")

__version__ = "0.0.2"
app.config["VERSION"] = __version__


if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler

    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(
        os.path.join(app.config["LOG_DIR"], "calendonator.log"), "midnight"
    )
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(
        logging.Formatter("<%(asctime)s> <%(levelname)s> %(message)s")
    )
    app.logger.addHandler(file_handler)

import calendonator.views
