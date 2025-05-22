"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

from service import routes
from service.common import log_handlers
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(50 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(50, "*"))
app.logger.info(50 * "*")
