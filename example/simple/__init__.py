from flask import jsonify
from flask.ext.debugtoolbar import DebugToolbarExtension

from flask_api_app import FlaskApiApp
from flask_api_app.core.api import api
from flask_api_app.extensions import oauth

app = FlaskApiApp(__name__)
app.config.from_pyfile('setting.cfg')
app.init_extensions()

debug_toolbar = DebugToolbarExtension()
debug_toolbar.init_app(app)


@api.route('/sample1')
@oauth.require_oauth('email')
def handle_sample1():
    return jsonify({'hello': 'world'})


app.register_core_blueprint(api=api, api_url_prefix='/api/v1.0')

if __name__ == '__main__':
    app.run(debug=True)
