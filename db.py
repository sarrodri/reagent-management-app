# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/ flask SQLAlchemy docs
# Note: Whoever works on this will need to run "pip install -U Flask-SQLAlchemy" into this directory
# Use comments please and thank youuuu

from flask_sqlalchemy import SQLAlchemy as sql
from sqlalchemy import create_engine
import app
import os

#import
db = sql(app)


#Create a reagent class 
class Reagent(db.Model):
    
    upc = db.Column(db.Integer(50), nullable=False)
    name = db.Column(db.String(50))
    expiration_date = db.Column(db.Date)
    initials = db.Column(db.String(3))

