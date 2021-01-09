import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enables debug mode.
DEBUG = True

# Connects to the database
SQLALCHEMY_DATABASE_URI = 'postgres://mcdczwsgmvrrdv:c0d960b1817b35a3b30e545a7b06f81df2dd193b24ab47b1c8db8f97b4871071@ec2-52-205-99-67.compute-1.amazonaws.com:5432/der1ug5f2c5p08'

SQLALCHEMY_TRACK_MODIFICATIONS = False


#'postgresql://postgres:lawpal86@localhost:5432/fyyur'

