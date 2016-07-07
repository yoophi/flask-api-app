import os
from flask import Blueprint, render_template

current_dir = os.path.dirname(__file__)
main = Blueprint('main', __name__, template_folder=os.path.join(current_dir, 'templates'))


@main.route('/')
def index():
    return render_template('index.html')
