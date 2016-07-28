import os
import os.path as op

from flask import jsonify
from flask_debugtoolbar import DebugToolbarExtension

from flask_api_app import FlaskApiApp
from flask_api_app.core.api import api
from flask_api_app.database import db
from flask_api_app.extensions import oauth

app = FlaskApiApp(__name__)

app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['DATABASE_FILE'] = 'sample_db.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = True

app.init_extensions()
db.init_app(app)

debug_toolbar = DebugToolbarExtension()
debug_toolbar.init_app(app)


@api.route('/sample1')
@oauth.require_oauth('email')
def handle_sample1():
    return jsonify({'hello': 'world'})


app.register_core_blueprint(api=api, api_url_prefix='/api/v1.0')


def build_sample_db():
    """
    Populate a small db with some example entries.
    """
    from flask.ext.api_app.core.accounts.models import User
    from flask.ext.api_app.core.api.models import Client

    db.drop_all()
    db.create_all()

    # Create sample User
    user = User()
    user.username = 'yoophi'
    user.email = user.username + "@example.com"
    user.password = 'secret'
    user.active = True
    db.session.add(user)

    # Create sample Client
    client = Client()
    client.name = 'client'
    client.user = user
    client.client_id = 'client'
    client.client_secret = 'secret'
    client.redirect_uris_text = 'http://example.com/'
    client.default_scopes_text = 'email'
    client.is_confidential = True
    db.session.add(client)

    db.session.commit()
    return


if __name__ == '__main__':
    # Build a sample db on the fly, if one does not exist yet.
    app_dir = op.realpath(os.path.dirname(__file__))
    database_path = op.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        with app.app_context():
            build_sample_db()

    # Start app
    app.run(debug=True)
