# -*- coding: utf-8 -*-
from .models import User, Role
from ...database import db
from ...extensions import admin
from ...helpers import ProtectedModelView

admin.add_view(ProtectedModelView(User, session=db.session, name='User', category='User'))
admin.add_view(ProtectedModelView(Role, session=db.session, name='Role', category='User'))

