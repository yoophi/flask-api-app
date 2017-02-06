# -*- coding: utf-8 -*-
from flask_mail import Mail
from flask_oauthlib.provider import OAuth2Provider
from flask_security import Security
from flask_admin import Admin
from .helpers import FlaskApiAppIndexView

security = Security()
mail = Mail()
oauth = OAuth2Provider()

admin = Admin(index_view=FlaskApiAppIndexView(), base_template='admin_base.html', template_mode='bootstrap3')
