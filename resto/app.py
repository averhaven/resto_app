"""This module contains creation of the flask app."""

from flask import Flask
from resto import restofind

def create_app():
    app = Flask(__name__)
    app.secret_key ='dev'
    
    app.register_blueprint(restofind.bp)

    return app