"""This module contains creation of the flask app."""

from flask import Flask
from resto import routes

def create_app(env="production"):
    app = Flask(__name__)
    app.secret_key ='dev'
    app.env = env
    
    app.register_blueprint(routes.bp)

    return app