from sweproject import app , db, auto
from flask_login import LoginManager
from flask import Flask,session, request, flash, url_for, redirect, render_template, abort ,g
from flask_login import login_user , logout_user , current_user , login_required
from models import User,Detected,Accepted,Rejected
from flask import jsonify
from datetime import datetime
import os
import shutil
import random

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
## Load the user from his user id
def load_user(id):
	return User.query.get(int(id))

@app.before_request
## Setting the logged in user
@auto.doc()
def before_request():
	g.user = current_user # return username in get_id()



@app.route('/')
@login_required
@auto.doc()
## Index page
def index():
	return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
@auto.doc()
## Function for login
def login():
	if g.user.is_authenticated:
		return redirect(url_for('home'))
	if request.method == 'GET':
		return render_template('login.html')
	username = request.form['username']
	password = request.form['password']
	registered_user = User.query.filter_by(username=username,password=password).first()
	if registered_user is None:
		flash('Username or Password is invalid' , 'error')
		return redirect(url_for('login'))
	login_user(registered_user)
	flash('Logged in successfully')
	return redirect(request.args.get('next') or url_for('home'))

@app.route('/home',methods=['GET'])
@auto.doc()
@login_required
## Home page
def home():
	return render_template('home.html')

@app.route('/logout')
@auto.doc()
## Function for logout
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/data.json',methods=['POST'])
@auto.doc()
## Retrieve detected images
def loadData():
	files = Detected.query.filter_by(cameraid=request.form['cameraid']).offset(request.form['skipcount']).all();
	temp = []
	for file in files:
		temp.append(file.serialize(getPathForFile(file.timestamp)))

	return jsonify(temp)

## Get file path from timestamp
def getPathForFile(timestamp):
	return '/images/' + random.choice(os.listdir("/Users/bharathyeddula/Desktop/backend/images/"))

@app.route('/delete',methods=['POST'])
@auto.doc()
## Move the detected file to the rejected DB
def delete():
	timestamp = request.form['timestamp']
	cameraid = request.form['cameraid']
	boundingbox = request.form['boundingbox']

	Detected.query.filter_by(timestamp=timestamp).filter_by(cameraid=cameraid).delete()
	db.session.commit()

	rejected = Rejected(timestamp,cameraid,boundingbox)
	db.session.add(rejected)
	db.session.commit()

	return "ok"

@app.route('/accept',methods=['POST'])
@auto.doc()
## Move the detected file to the accepted DB
def accept():
	timestamp = request.form['timestamp']
	cameraid = request.form['cameraid']
	boundingbox = request.form['boundingbox']

	Detected.query.filter_by(timestamp=timestamp).filter_by(cameraid=cameraid).delete()

	accepted = Accepted(timestamp,cameraid,boundingbox)
	db.session.add(accepted)
	db.session.commit()

	return "ok"

@app.route('/documentation')
def documentation():
    return auto.html()