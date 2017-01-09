# -*- coding: utf-8 -*-
from flask import request, render_template, redirect, current_app
from flask_login import login_required, current_user

from . import api
from .models import Client
from ...extensions import oauth


def get_current_user():
    User = current_app.user_model
    return User.query.get(current_user.id)


@api.route('/oauth/authorize', methods=['GET', 'POST'])
@login_required
@oauth.authorize_handler
def oauth_authorize(*args, **kwargs):
    user = get_current_user()
    if not user:
        return redirect('/')

    if request.method == 'GET':
        client_id = kwargs.get('client_id')
        client = Client.query.filter_by(client_id=client_id).first()
        kwargs['client'] = client
        kwargs['user'] = user
        return render_template('authorize.html', **kwargs)

    confirm = request.form.get('confirm', 'no')
    return confirm == 'yes'


@api.route('/oauth/token', methods=['GET', 'POST'])
@oauth.token_handler
def oauth_access_token():
    return None
