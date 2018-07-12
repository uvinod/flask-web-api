import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize application
app = Flask(__name__, static_folder=None)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

# Initialize Flask SQL Alchemy
db = SQLAlchemy(app)

# Register blue prints
from app.bucket import bucket
app.register_blueprint(bucket, url_prefix = '/api')