from sweproject import db
from datetime import datetime
from sweproject import app

## Model class for users db
class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)

## Model class for detected DB
class Detected(db.Model):
    __tablename__ = "detected"
    timestamp = db.Column('time_stamp' , db.TEXT, primary_key=True)
    cameraid = db.Column('camera_id' , db.TEXT, primary_key=True)
    x = db.Column('x' , db.Float)
    y = db.Column('y' , db.Float)
    width = db.Column('width' , db.Float)
    height = db.Column('height' , db.Float)

    def __init__(self , timestamp ,cameraid, x, y, width, height):
        self.timestamp = timestamp
        self.cameraid = cameraid
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        

    def serialize(self,filepath):
        return {
            'timestamp' : self.timestamp,
            'cameraid' : self.cameraid,
            'x' : self.x,
            'y' : self.y,
            'width' : self.width,
            'height' : self.height,
            'filepath' : filepath
        }

## Model class for accepted DB
class Accepted(db.Model):
    __tablename__ = "accepted"
    timestamp = db.Column('time_stamp' , db.TEXT, primary_key=True)
    cameraid = db.Column('camera_id' , db.TEXT, primary_key=True)
    x = db.Column('x' , db.Float)
    y = db.Column('y' , db.Float)
    width = db.Column('width' , db.Float)
    height = db.Column('height' , db.Float)

    def __init__(self , timestamp ,cameraid, x, y, width, height):
        self.timestamp = timestamp
        self.cameraid = cameraid
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        

    def serialize(self,filepath):
        return {
            'timestamp' : self.timestamp,
            'cameraid' : self.cameraid,
            'x' : self.x,
            'y' : self.y,
            'width' : self.width,
            'height' : self.height,
            'filepath' : filepath
        }
        
## Model class for rejected DB
class Rejected(db.Model):
    __tablename__ = "rejected"
    timestamp = db.Column('time_stamp' , db.TEXT, primary_key=True)
    cameraid = db.Column('camera_id' , db.TEXT, primary_key=True)
    x = db.Column('x' , db.Float)
    y = db.Column('y' , db.Float)
    width = db.Column('width' , db.Float)
    height = db.Column('height' , db.Float)

    def __init__(self , timestamp ,cameraid, x, y, width, height):
        self.timestamp = timestamp
        self.cameraid = cameraid
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        

    def serialize(self,filepath):
        return {
            'timestamp' : self.timestamp,
            'cameraid' : self.cameraid,
            'x' : self.x,
            'y' : self.y,
            'width' : self.width,
            'height' : self.height,
            'filepath' : filepath
        }
