# -*- coding: utf-8 -*-
from flask_admin import Admin
from flask_mail import Mail
from flask_oauthlib.provider import OAuth2Provider
from flask_security import Security, SQLAlchemyUserDatastore

from .core.accounts.models import Role, User
from .database import db
from .helpers import ProtectedAdminIndexView


class FlaskApiAppIndexView(ProtectedAdminIndexView):
    pass


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore)

admin = Admin(index_view=FlaskApiAppIndexView(),
              base_template='admin_base.html')

mail = Mail()
oauth = OAuth2Provider()


def init_extensions(app):
    for ext in (db, admin, security, mail, oauth,):
        getattr(ext, 'init_app')(app)
