# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/ flask SQLAlchemy docs
# Note: Whoever works on this will need to run "pip install -U Flask-SQLAlchemy" into this directory
# Use comments please and thank youuuu

from flask_sqlalchemy import SQLAlchemy as sql
from sqlalchemy import create_engine
import app
import os

#import
db = sql(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://reagent_app:password@localhost/reagentLabelDB' # fill in with correct url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #keeps it from complaining in the console

#Create a reagent class 
class Reagent(db.Model):
    
    # label table
    upc = db.Column(db.Integer(10), nullable=False)
    initials = db.Column(db.String(5))
    openedDate = db.Column(db.Date)
    expirationDate = db.Column(db.Date)
    initials = db.Column(db.String(5))
    lot = db.Column(db.Integer)
    reagent = db.Column(db.String(50))
    # reagentExpiration table
    # reagent is foreign key
    expiration = db.Column(db.Integer(10))