from flask import Flask
from os import environ
from waitress import serve
from controllers.student_controller import student_controller

app = Flask(__name__)

app.register_blueprint(student_controller, url_prefix="/students")


def start_server(host="0.0.0.0", port=8000):
    if environ.get("FLASK_ENV") != "production":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
