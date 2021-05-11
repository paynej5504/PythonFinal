#import statements
from flask_login import UserMixin
from . import db

# create user model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True) #required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# create entry model
class Entry( db.Model):
    houseId = db.Column(db.String(100))
    date = db.Column(db.Date)
    id = db.Column(db.Integer, db.ForeignKey('user.id'))
    eggs = db.Column(db.Integer)
    alive = db.Column(db.Integer)
    dead = db.Column(db.Integer)
    species = db.Column(db.String(100))
    cowbird = db.Column(db.String(100))
    damaged = db.Column(db.String(100))
    comment = db.Column(db.String(2000))
    entryId = db.Column(db.Integer, primary_key=True)
