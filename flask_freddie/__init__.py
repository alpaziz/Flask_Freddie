from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets

app = Flask(__name__)

#Secret token
app.config['SECRET_KEY']				=	secrets.token_hex(16)

# Will be stored in current directory
app.config['SQLALCHEMY_DATABASE_URI']	= 'sqlite:///site.db'


# Create DB
db = SQLAlchemy(app)

from flask_freddie import routes