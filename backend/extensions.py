from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from redis import Redis

# Loading environment variables
load_dotenv()

# Flask-JWT-Extended
# https://flask-jwt-extended.readthedocs.io/en/stable/
jwt = JWTManager()

# Redis
# https://pypi.org/project/redis/
redis_client = Redis(host="cache", port=6379)