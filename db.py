# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/ flask SQLAlchemy docs
# Note: Whoever works on this will need to run "pip install -U Flask-SQLAlchemy" into this directory
# Use comments please and thank youuuu

from flask_sqlalchemy import SQLAlchemy as sql
import app

#import
db = sql(app)

#Create a reagent class 
class Reagent(db.Model):
    # in here, we will shape the data from the api into a database
    #Example (I think):
    
    emplid = db.Column(db.String(100), nullable=False)
    lot_number = db.Column(db.String(50))
    expiration_date = db.Column(db.Date)
    storage_location = db.Column(db.String(100))

