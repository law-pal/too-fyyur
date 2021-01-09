import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enables debug mode.
DEBUG = True

# Connects to the database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:lawpal86@localhost:5432/fyyur'

SQLALCHEMY_TRACK_MODIFICATIONS = False


#'postgresql://postgres:lawpal86@localhost:5432/fyyur'

