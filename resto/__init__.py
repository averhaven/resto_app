from flask import Flask, render_template
from resto import restofind

def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        person = "Alex"
        return render_template("hello.html", person=person)
    
    app.register_blueprint(restofind.bp)

    return app