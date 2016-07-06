from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/sample')
def handle_sample():
    return jsonify({'out': 'sample api'})


from . import authentication
