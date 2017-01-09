# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask
from flask_security import SQLAlchemyUserDatastore
from wtforms import StringField
from wtforms.widgets import PasswordInput
from .database import db
from .extensions import admin, security, mail, oauth
from .helpers import ProtectedModelView, form_description

__version__ = '0.1.0'


class UserAdminView(ProtectedModelView):
    column_display_pk = True
    column_default_sort = ('id', True)

    form_excluded_columns = ()

    column_list = ('id', 'email', 'username', 'active', 'confirmed_at', 'login_count',)
    column_searchable_list = ('email',)

    form_rules = (
        'username', 'email', 'roles', 'active', 'dob', 'gender',
        'newpassword', form_description('비밀번호를 새로 지정하실 때만 입력해주세요.'),
        'confirmed_at',)

    form_extra_fields = {
        "newpassword": StringField(widget=PasswordInput())
    }

    def _show_missing_fields_warning(self, text):
        # suppress missing fields warning
        pass

    def on_model_change(self, form, model, **kwargs):
        if model.newpassword:
            setpwd = model.newpassword
            del model.newpassword

            model.set_password(setpwd)
            db.session.add(model)
            db.session.commit()


class RoleAdminView(ProtectedModelView):
    form_excluded_columns = ('users',)


class FlaskApiApp(Flask):
    def __init__(self, import_name, static_path=None, static_url_path=None, static_folder='static',
                 template_folder='templates', instance_path=None, instance_relative_config=False):
        super(FlaskApiApp, self).__init__(import_name, static_path, static_url_path, static_folder, template_folder,
                                          instance_path, instance_relative_config)
        self.role_model = None
        self.user_model = None
        self.role_admin_view = None
        self.user_admin_view = None

    def init_extensions(self, user_model=None, role_model=None, user_admin_view=None, role_admin_view=None):
        db.init_app(self)
        admin.init_app(self)

        if not role_model:
            from .core.accounts.models import Role as role_model

        if not user_model:
            from .core.accounts.models import User as user_model

        if not role_admin_view:
            role_admin_view = RoleAdminView

        if not user_admin_view:
            user_admin_view = UserAdminView

        self.role_model = role_model
        self.user_model = user_model
        self.role_admin_view = role_admin_view
        self.user_admin_view = user_admin_view

        user_datastore = SQLAlchemyUserDatastore(db, user_model, role_model)
        security.init_app(self, datastore=user_datastore)
        mail.init_app(self)
        oauth.init_app(self)

    def register_core_blueprint(self, api=None, api_url_prefix='/api',
                                main=None, main_url_prefix=''):
        from .core.api import api as api_blueprint
        from .core.main import main as main_blueprint

        api_blueprint = api or api_blueprint
        main_blueprint = main or main_blueprint

        admin.add_view(self.user_admin_view(self.user_model, session=db.session, name='User', category='User'))
        admin.add_view(self.role_admin_view(self.role_model, session=db.session, name='Role', category='User'))

        from .core.api import admin as api_admin

        self.register_blueprint(api_blueprint, url_prefix=api_url_prefix)
        self.register_blueprint(main_blueprint, url_prefix=main_url_prefix)
