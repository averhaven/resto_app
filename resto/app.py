"""This module contains creation of the flask app."""

from flask import Flask, g
from resto import routes, maps_client
from resto.secret_key import get_secret_key

def create_app(env="production"):
    app = Flask(__name__)
    app.secret_key ='dev'
    app.env = env
    
    app.register_blueprint(routes.bp)

    return app