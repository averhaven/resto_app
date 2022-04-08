from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        person = "Alex"
        return render_template("hello.html", person=person)
    
    @app.route('/')
    def start_page():
        return render_template("restofind.html")

    return app