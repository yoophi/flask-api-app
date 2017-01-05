from flask import Blueprint, current_app
from flask.ext.login import current_user

api = Blueprint('api', __name__)

from . import authentication, views
