from flask import Flask, render_template
from resto import restofind

def create_app():
    app = Flask(__name__)
    app.secret_key ='dev'
    
    app.register_blueprint(restofind.bp)

    return app