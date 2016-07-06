from flask import jsonify

from rest_flask import RestFlask
from rest_flask.extensions import oauth

app = RestFlask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:5432/example'
app.config['SECRET_KEY'] = 'secret'
app.init_extensions()

api = app.blueprints['api']


@api.route('/sample1')
@oauth.require_oauth('email')
def handle_sample1():
    return jsonify({'hello': 'world'})


app.register_blueprint(api, url_prefix='/api/v1.0')

if __name__ == '__main__':
    app.run(debug=True)
