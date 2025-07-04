from flask import Flask

from wsgi import start_server
from extensions import jwt
from settings import settings_from_server, type_server

from controllers.user_controller import user_controller
from controllers.blog_controller import blog_controller

# Flask
# https://flask.palletsprojects.com/en/stable/
app = Flask(__name__)

# Settings
jwt.init_app(app)
app.config.from_object(settings_from_server[type_server])

# Blueprints
app.register_blueprint(user_controller)
app.register_blueprint(blog_controller)

if __name__ == "__main__":
    start_server(app)