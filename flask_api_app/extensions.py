# -*- coding: utf-8 -*-
from flask.ext.admin import Admin
from flask.ext.cors import CORS
from flask.ext.mail import Mail
from flask.ext.marshmallow import Marshmallow
from flask.ext.oauthlib.provider import OAuth2Provider
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask_bootstrap import Bootstrap

from flask_api_app.core.accounts.models import Role, User
from flask_api_app.database import db

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore)

admin = Admin()
cors = CORS()
ma = Marshmallow()
mail = Mail()
oauth = OAuth2Provider()
bootstrap = Bootstrap()


def init_extensions(app):
    for ext in (db, admin, security, cors, ma, mail, oauth, bootstrap,):
        getattr(ext, 'init_app')(app)
