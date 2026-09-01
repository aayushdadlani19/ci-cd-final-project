"""
Package Initialization
"""

from flask import Flask

app = Flask(__name__)

from service.common import log_handlers
log_handlers.init_logging(app, "gunicorn.error")

from service.common import error_handlers  # noqa: E402,F401
from service import routes  # noqa: E402,F401
