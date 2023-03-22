from flask import Flask, render_template
from config import Config
from .site.routes import site

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from helpers import JSONEncoder

app = Flask(__name__)
CORS(app)

app.register_blueprint(site)


