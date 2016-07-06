# -*- coding: utf-8 -*-
from flask.ext.admin.contrib import sqla

from rest_flask.database import db
from rest_flask.extensions import admin
from .models import Client, Token

admin.add_view(sqla.ModelView(Client, session=db.session, name='Client'))
admin.add_view(sqla.ModelView(Token, session=db.session, name='Token'))

