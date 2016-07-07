# -*- coding: utf-8 -*-
from flask.ext.admin.contrib import sqla

from flask_api_app.database import db
from flask_api_app.extensions import admin
from .models import User, Role

admin.add_view(sqla.ModelView(User, session=db.session, name='User', category='User'))
admin.add_view(sqla.ModelView(Role, session=db.session, name='Role', category='User'))

