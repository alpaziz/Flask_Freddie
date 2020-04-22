from flask import render_template, url_for, flash, redirect
from flask_freddie import app, db
from flask_freddie.forms import RegistrationForm
from flask_freddie.models import User


@app.route("/")
def index():
	return(render_template("home.html"))


@app.route("/register", methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username = form.username.data, email = form.email.data)
		db.session.add(user)
		db.session.commit()
		flash('Your account has been created!', 'success')
		return redirect(url_for('index'))
	return(render_template("register.html", title = "Register", form = form))

# @app.route("/g")
# def getEnpoint():
# 	# Get	
# 	return("<h2>Hello I am your api\n</h2>")


# @app.route("/p", methods=['POST'])
# def postEndpoint():
# 	return("I received your message, I will reply when I can\n")
