# coding: utf-8
from __future__ import print_function, unicode_literals

from flask import redirect
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import rules
from flask_login import current_user
from flask_security import url_for_security
from markupsafe import Markup


class AuthRoleMixin(object):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_admin_privs

    def _handle_view(self, name, **kwargs):
        next_url = '/admin'
        if self.url:
            next_url = self.url

        if not current_user.is_authenticated:
            return redirect(url_for_security('login', next=next_url))

        if not self.is_accessible():
            return self.inaccessible_callback(name, **kwargs)


class ProtectedAdminIndexView(AuthRoleMixin, AdminIndexView):
    @expose('/')
    def index(self):
        return super(ProtectedAdminIndexView, self).index()


class ProtectedModelView(AuthRoleMixin, ModelView):
    pass


def _view_img(width=80, type='circle'):
    if type not in ('circle', 'rounded', 'thumbnail',):
        type = 'circle'

    def f(view, context, model, name):
        # 이미지 출력
        image = getattr(model, name)
        return Markup('<img src="%s" width="%d" class="img-responsive img-%s">' % (image, width, type,)) \
            if image else ''

    return f


def get_or_create(session, model, **kwargs):
    """
    Creates an object or returns the object if exists
    credit to Kevin @ StackOverflow
    from: http://stackoverflow.com/questions/2546207/does-sqlalchemy-have-an-equivalent-of-djangos-get-or-create
    """

    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        return instance


class FlaskApiAppIndexView(ProtectedAdminIndexView):
    pass


def form_description(text):
    tpl = '<div class="control-group" style="margin-top: -1em">' \
          '<div class="control-label"></div>' \
          '<div class="controls">{text}</div></div>'

    return rules.HTML(tpl.format(text=text))
