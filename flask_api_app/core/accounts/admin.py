# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask.ext.admin.form import rules
from wtforms import StringField
from wtforms.widgets import PasswordInput

from .models import User, Role
from ...database import db
from ...extensions import admin
from ...helpers import ProtectedModelView


def form_desc(text):
    tpl = '<div class="control-group" style="margin-top: -1em">' \
          '<div class="control-label"></div>' \
          '<div class="controls">{text}</div></div>'

    return rules.HTML(tpl.format(text=text))


class UserAdminView(ProtectedModelView):
    column_display_pk = True
    column_default_sort = ('id', True)

    form_excluded_columns = ()

    column_list = ('id', 'email', 'username',
                   'active', 'confirmed_at', 'login_count',)

    column_searchable_list = ('email',)

    form_rules = (
        'username', 'email', 'roles', 'active', 'dob', 'gender',
        'newpassword', form_desc('비밀번호를 새로 지정하실 때만 입력해주세요.'),
        'confirmed_at', 'current_login_at', 'current_login_ip', 'login_count',)

    form_extra_fields = {
        "newpassword": StringField(widget=PasswordInput())
    }

    def on_model_change(self, form, model, **kwargs):
        if model.newpassword:
            setpwd = model.newpassword
            del model.newpassword

            model.set_password(setpwd)
            db.session.add(model)
            db.session.commit()


class RoleAdminView(ProtectedModelView):
    form_excluded_columns = ('users',)


admin.add_view(UserAdminView(User, session=db.session, name='User', category='User'))
admin.add_view(RoleAdminView(Role, session=db.session, name='Role', category='User'))
