from flask import Flask

from settings import settings_from_server, type_server
from wsgi import start_server

from controllers.user_controller import user_controller

# Flask
# https://flask.palletsprojects.com/en/3.0.x/
app = Flask(__name__)
app.config.from_object(settings_from_server[type_server])

# Blueprints
app.register_blueprint(user_controller)

if __name__ == "__main__":
    start_server(app)