from datetime import datetime

from flask_security import RoleMixin as BaseRoleMixin, UserMixin as BaseUserMixin
from flask_security.utils import encrypt_password
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column('created_at', db.DateTime, nullable=False,
                           default=datetime.now)
    updated_at = db.Column('updated_at', db.DateTime, nullable=False,
                           default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return '<{self.__class__.__name__}:{self.id}>'.format(self=self)


class RoleMixin(BaseRoleMixin):
    @classmethod
    def createrole(cls, session, name, description=''):
        role = cls(name=name, description=description)
        session.add(role)

        return role

    def __repr__(self):
        return '<{self.__class__.__name__}:{self.name}>'.format(self=self)


class UserMixin(BaseUserMixin):
    @property
    def has_admin_privs(self):
        for role in self.roles:
            if role.name.lower() == 'admin':
                return True

        return False

    @classmethod
    def createuser(cls, session, email, password, roles=None):
        user = cls(email=email, active=True)
        user.set_password(password)

        if roles:
            user.roles = roles

        session.add(user)
        return user

    def set_password(self, password):
        self.password = encrypt_password(password)

    def __repr__(self):
        return '<{self.__class__.__name__}:{self.email}>'.format(self=self)
