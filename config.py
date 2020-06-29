import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# const for base directory
app_dir = os.path.dirname(os.path.realpath(__file__))


# making app instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'

# disable track modifications due to errors in logs
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize extensions
db = SQLAlchemy(app)
