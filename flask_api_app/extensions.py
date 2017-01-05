# -*- coding: utf-8 -*-
from flask_admin import Admin
from flask_mail import Mail
from flask_oauthlib.provider import OAuth2Provider
from flask_security import Security

from flask.ext.api_app.helpers import FlaskApiAppIndexView

security = Security()
admin = Admin(index_view=FlaskApiAppIndexView(), base_template='admin_base.html')
mail = Mail()
oauth = OAuth2Provider()
