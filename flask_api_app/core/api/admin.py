# -*- coding: utf-8 -*-
from flask_admin.contrib import sqla

from flask_api_app.database import db
from flask_api_app.extensions import admin
from .models import Client, Token

admin.add_view(sqla.ModelView(Client, session=db.session, name='Client'))
admin.add_view(sqla.ModelView(Token, session=db.session, name='Token'))

