from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_autodoc import Autodoc

## configurw the app object
app = Flask(__name__)
auto = Autodoc(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/sweproject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/Users/bharathyeddula/Desktop/backend/images/'
app.debug = True

## configure the sqlalchemy db object
db = SQLAlchemy(app)

from views import *
 
 ## run the app
if __name__ == '__main__':
	app.secret_key = 'sup sec key'
	app.run()