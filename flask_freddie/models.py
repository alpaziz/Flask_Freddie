from flask_freddie import db
from datetime import datetime


class User(db.Model):
	# Create columns
	id 			= db.Column(db.Integer, primary_key = True)
	username    = db.Column(db.String(20), unique=True, nullable=False) 
	email       = db.Column(db.String(120), unique=True, nullable=False) 
	#FOR LOAN
	# date_added  = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)



	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"
