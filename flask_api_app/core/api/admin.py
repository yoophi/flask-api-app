# -*- coding: utf-8 -*-
from .models import Client, Token
from ...database import db
from ...extensions import admin
from ...helpers import ProtectedModelView

admin.add_view(ProtectedModelView(Client, session=db.session, name='Client'))
admin.add_view(ProtectedModelView(Token, session=db.session, name='Token'))

