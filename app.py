from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime as dt, timedelta
import os
import random
from upc_functions import generate_product_number, generate_upc
from sqlalchemy import MetaData, create_engine, Table, text, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from db import Reagent, reagentExpiration

Base = declarative_base()
# This is where we will make the API using Flask and Python
# Docs: https://flask.palletsprojects.com/en/3.0.x/
# Whoever works on this will need to run "pip install flask" in the command line
# use comments please n thank youuuuuuuuuuu <3

# PUSHING to main branch:
#     -save your work
#     -git pull origin main

#   important note: (if you try to push or
#                   commit before pulling, 
#                   bad things happen and
#                   I will come after you)
#     -git add .
#     -git commit -m "your comment here"
#     -git push origin main

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://reagent_app:password@localhost/reagentLabelDB' # fill in with correct url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #keeps it from complaining in the console

db.init_app(app)

class Reagent(db.Model):
    __table__ = Reagent
    
    def __init__(self, upc, initials, lot, reagent, openedDate, expirationDate):
        self.upc = upc
        self.initials = initials
        self.lot = lot
        self.reagent = reagent
        self.openedDate = openedDate
        self.expirationDate = expirationDate

class reagentExpiration(db.Model):
    __table__ = reagentExpiration

    def __init__(self, reagent,expirationDate):
        self.reagent = reagent
        self.expirationDate = expirationDate

expiration_rules = {
    'L1 UF Heparin': 1,
    'L2 UF Heparin': 1,
    'L1 LMW Heparin': 1,
    'L2 LMW Heparin': 1,
    'Low Fib': 1,
    'ABN 3': 1,
    'Factory Diluent (Aliquaot)': 30,
    'Norm 1': 1,
    'Diluted Clean B': None, #handling with no expiration dates
    'R2g': 10,
    'SynthASil': 10,
    'CaCl': None,
    'D-Dimer reagent': 7,
    'Dimer Latex': 7,
    'QFA': 7,
    'Anti XA': 4,
    'Anti XA-Sub': None,
    'Rinse Solution': 30,
    'Cleaning Solution': 30,
    'Factory Diluent (Bottle)': 7,
    'Cleaning Agent': 30,
    'L1 ESR Check': 7,
    'L2 ESR Check': 7,
    'Anti A': None,
    'Anti B': None,
    'Anti D (Series 4)': None,
    'Anti D (Series 5)': None,
    'Monoclonal Control': None,
    'Panel Screen 1': None,
    'Panel Screen 2': None,
    'Panel Screen 3': None,
    'A Cells': None,
    'B Cells': None,
    'Anti IgG': None,
    'Poly': None,
    'N-Hance': None,
    'PeG': None,
    'Compliment Control': None,
    'Anti C3d': None,
    'Ortho Anti D': None,
    'Check Cell': None
}

# Retrieve all reagents endpoint
@app.route('/', methods=['POST','GET'])
def get_reagents():
    today = dt.today().date()
    reagents = Reagent.query.filter(Reagent.expirationDate <= today).all()
    reagent_names = list(expiration_rules.keys())  # Extract reagent names from expiration_rules
    return render_template('Homepage.html', reagents=reagents, reagent_names=reagent_names) #send render to actual html page

# Retrieve reagent by specific search (need to decide what to search by, filling in with ID)
@app.route('/<int:upc>', methods=['GET'])
def search_reagent(upc):
    reagent = Reagent.query.get(upc)
    if reagent:
        return render_template('Homepage.html', reagent = reagent.serialize())
    else:
        return render_template('Homepage.html', message= 'Reagent not found'), 404


@app.route('/add', methods=['POST'])
def add_reagent():
    form_data = request.get_json()
    reagent = form_data.get('reagent_name') #is 'name' a drop down?
    initials = form_data.get('Initials')  # Get initials from request data
    lot = form_data.get('lotNumber')
    openedDate = dt.now() #time stamp for date opened
    print("hi method")
    print(request.method)
 # Generate UPC for the new reagent
    company_prefix = 123 
    product_number = generate_product_number()
    upc = generate_upc(company_prefix, product_number)

    # if the reagent name is in the expiration rules
    expiration_date = None
    if reagent in expiration_rules:
        expiration_days = expiration_rules[reagent]
        if expiration_days is not None:  # Check if expiration_days is defined
            expiration_date = dt.now() + timedelta(days=expiration_days)
# TODO: Add in error handling because there can't be any null data
    new_reagent_expiration = reagentExpiration(reagent=reagent, expirationDate = expiration_date)
    db.session.add(new_reagent_expiration)
    db.session.commit()

    new_reagent = Reagent(initials=initials,
                          openedDate = openedDate,
                          expirationDate=expiration_date,                    
                          upc=upc,
                          lot=lot, reagent=reagent)
    db.session.add(new_reagent)
    db.session.commit()
    return ("Good"), 201

@app.route('/<int:upc>', methods=['POST','GET']) #Get and post?
def print_reagent(upc):
    reagent = Reagent.query.get(upc)
    if reagent:        
        return jsonify({
            'upc': reagent.upc,
            'lot': reagent.lot,
            'expirationDate': reagent.expirationDate if reagent.expirationDate else None
        }), 200
    else:
        return jsonify({'message': 'Reagent not found'}), 404


# delete an existing reagent
@app.route('/<int:upc>', methods=['DELETE'])
def delete_reagent(upc): #filled in via scan
    reagent = Reagent.query.get(upc)
    if reagent:
        db.session.delete(reagent)
        db.session.commit()
        return render_template('Homepage.html', message = 'Reagent deleted')
    else:
        return render_template('Homepage.html', message='Reagent not found'), 404

if __name__ == '__main__': #don't run debugger in production, only for testing
    app.run(debug=True)