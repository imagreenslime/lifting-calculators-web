import requests
import configparser
from flask import Flask
from os import path


def create_app():
    app = Flask(__name__)
    from views import views
    app.register_blueprint(views, url_prefix = '/')
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

