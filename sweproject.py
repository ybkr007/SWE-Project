from flask import Flask
from flask_sqlalchemy import SQLAlchemy

## configurw the app object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sweproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

## configure the sqlalchemy db object
db = SQLAlchemy(app)

from views import *
 
 ## run the app
if __name__ == '__main__':
	app.secret_key = 'sup sec key'
	app.run()