# coding: utf-8

from __future__ import unicode_literals, print_function

import sys

from flask import current_app
from flask_script import prompt, prompt_pass, prompt_choices

from .models import Role, User
from ...database import db
from ...helpers import get_or_create
from ...manage import Manager

manager = Manager(current_app)


@manager.command
@manager.option('-n', '--name', help='Role name')
@manager.option('-d', '--description', help='Role description')
def createrole(name=None, description=None):
    """Create a role"""

    if not name:
        name = prompt("Role Name")

    if not description:
        description = prompt("Role description")

    if all([name, description]):
        role = Role.createrole(
            db.session,
            name=name,
            description=description
        )
        db.session.commit()
    else:
        role = "Can't create the role"

    print(role)


@manager.command
@manager.option('-e', '--email', help='User e-mail')
@manager.option('-p', '--password', help='User password')
def createsuperuser(email=None, password=None):
    """Create a supersuer"""

    if not email:
        email = prompt("A valid email address")

    if not password:
        password = prompt_pass("Password")

    if all([email, password]):
        admin = get_or_create(db.session, Role, name='admin')
        user = User.createuser(db.session, email, password, roles=[admin])
        db.session.commit()
    else:
        user = "Can't create the supersuser"

    print(user)


@manager.command
@manager.option('-e', '--email', help='User e-mail')
@manager.option('-p', '--password', help='User password')
@manager.option('-r', '--role', help='User role')
def createuser(email=None, password=None, role=None):
    """Create a user"""

    if not email:
        email = prompt("A valid email address")

    if not password:
        password = prompt_pass("Password")

    if not role:
        roles = [r.name for r in db.session.query(Role)]
        role_name = prompt_choices("Role", choices=roles,
                                   no_choice=('none', ''))
        if role_name:
            role = get_or_create(db.session, Role, name=role_name)
        else:
            role = None
    else:
        role = get_or_create(db.session, Role, name=role)

    if all([email, password]):
        user = User.createuser(db.session, email, password, roles=[role])
        db.session.commit()
    else:
        user = "Can't create the user"

    print(user)


@manager.command
@manager.option('-e', '--email', help='User e-mail')
@manager.option('-p', '--password', help='User password')
def modifypassword(email=None, password=None):
    """비밀번호 변경"""

    if not email:
        email = prompt("A valid email address")

    if not password:
        password = prompt_pass("Password")

    if all([email, password]):
        user = User.query.filter_by(email=email).first()

        if not user:
            print('Invalid user <{email}>'.format(email=email))
            sys.exit(0)

        user.set_password(password)
        db.session.add(user)
        db.session.commit()
    else:
        user = "xxx"

    print(user)
