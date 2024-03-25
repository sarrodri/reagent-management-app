from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
import json
import datetime as dt, timedelta
import os

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

# need to configure sqlalchemy with the flask app
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name' # fill in with correct url
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #keeps it from complaining in the console

#initialize
db = SQLAlchemy(app)

#Create a reagent class 
class Reagent(db.Model):
    
    upc = db.Column(db.Integer(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    expiration_date = db.Column(db.Date,nullable=False)
    initials = db.Column(db.String(3),nullable=False)

# Retrieve all reagents endpoint
@app.route('/home', methods=['GET'])
def get_reagents():
    today = dt.today().date()
    reagents = Reagent.query.filter(Reagent.exp_date <= today).all()
    return render_template([reagent.serialize() for reagent in reagents])

# Retrieve reagent by specific search (need to decide what to search by, filling in with ID)
@app.route('/<int:reagent_id>', method=['GET'])
def search_reagent(reagent_id):
    reagent = Reagent.query.get(reagent_id)
    if reagent:
        return render_template(reagent.serialize())
    else:
        return render_template({'message': 'Reagent not found'}), 404


# Define a mapping of reagent names to exp_date
expiration_rules = {
    'L1 UF Heparin': 1, #need to get full list of reagent names and exp_dates
    'L2 UF Heparin' : 1,
    'L1 LMW Heparin' : 1,
    'L2 LMW Heparin' : 1,
    'ABN 3': 1,
    'Anti XA' : 1,
    'Anti XA-Sub': 1,
    'Factory Diluent (Bottle)': 7
}

@app.route('/add', methods=['POST'])
def add_reagent():
    data = request.json
    name = data.get('name') #is 'name' a drop down?
    initials = data.get('initials')  # Get initials from request data
    upc = data.get('upc') #UPC is filled in via scan
    
    # if the reagent name is in the expiration rules
    if name in expiration_rules:
        expiration_days = expiration_rules[name]
        expiration_date = dt.now() + timedelta(days=expiration_days)
    else:
        expiration_date = None
    
    new_reagent = Reagent(name=name, exp_date=expiration_date, initials=initials, upc=upc) #also need initials and UPC
    db.session.add(new_reagent)
    db.session.commit()
    return render_template(new_reagent.serialize()), 201

# update an existing reagent - updating update the initials?
# @app.route('reagents/add', method = ['POST'])
# def update_reagent(reagent_id):
#     reagent = Reagent.query.get(reagent_id)
#     if reagent:
#         data = 
#         reagent.name = data.get('name', reagent.name)
#         #fill in other criteria
#         db.session.commit()
#         return jsonify(reagent.serialize())
#     else:
#         return jsonify({'message': 'Reagent not found'}), 404

# delete an existing reagent - retain history of deleted reagents?
@app.route('/<int:upc>', methods=['DELETE'])
def delete_reagent(upc): #filled in via scan
    reagent = Reagent.query.get(upc)
    if reagent:
        db.session.delete(reagent)
        db.session.commit()
        return render_template({'message': 'Reagent deleted'})
    else:
        return render_template({'message': 'Reagent not found'}), 404

if __name__ == '__main__': #don't run debugger in production, only for testing
    app.run(debug=True)