import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
# Local database url
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/fyyurappdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False
