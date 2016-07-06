from flask import jsonify
from flask.ext.debugtoolbar import DebugToolbarExtension

from rest_flask import RestFlask
from rest_flask.core.api import api
from rest_flask.extensions import oauth

app = RestFlask(__name__)
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
