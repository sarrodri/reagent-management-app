from flask import Flask, jsonify
import json
from db import db, Reagent

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

# possibly use forms to intake info or engineers have data for us to import?
dummy_data = [ { 'id': 1, 'name': 'Sarah' }, { 'id': 2, 'name': 'Megan' }, { 'id': 3, 'name': 'Aly' }]

# full view endpoint
@app.route('/dummy_data', methods = ["GET"])
def index():
    return jsonify(dummy_data)

# need to configure sqlalchemy with the flask app
app.config['SQLALCHEMY_DATABASE_URI'] = #'mysql://username:password@localhost/db_name'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #dunno what this is

#initialize
db.init_app(app)

#log in page

# Retrieve all reagents endpoint
@app.route('/reagents/home', method=['GET'])
def get_reagents():
    reagents = Reagent.query.all()
    return jsonify([reagent.serialize() for reagent in reagents]) # serialize() converts sqlalchemy objects into serializable dicts


# Retrieve reagent by specific search (need to decide what to search by, filling in with ID)
@app.route('/reagents/<int:reagent_id>', method=['GET'])
def search_reagent(reagent_id):
    reagent = Reagent.query.get(reagent_id)
    if reagent:
        return jsonify(reagent.serialize())
    else:
        return jsonify({'message': 'Reagent not found'}), 404

# add a new reagent endpoint - automatically fill in the initials of the logged in user
@app.route('reagents/add', method = ['POST'])
def add_reagent():
    data = 
    new_reagent = 
    db.session.add(new_reagent)
    db.session.commit()
    return jsonify(new_reagent.serialize()), 201 # have this redirect to homepage and display a success message
    
# update an existing reagent - updating update the initials?
@app.route('reagents/add', method = ['POST'])
def update_reagent(reagent_id):
    reagent = Reagent.query.get(reagent_id)
    if reagent:
        data = 
        reagent.name = data.get('name', reagent.name)
        #fill in other criteria
        db.session.commit()
        return jsonify(reagent.serialize())
    else:
        return jsonify({'message': 'Reagent not found'}), 404

# delete an existing reagent - retain history of deleted reagents
@app.route('/reagents/<int:reagent_id>', methods=['DELETE'])
def delete_reagent(reagent_id):
    reagent = Reagent.query.get(reagent_id)
    if reagent:
        db.session.delete(reagent)
        db.session.commit()
        return jsonify({'message': 'Reagent deleted'})
    else:
        return jsonify({'message': 'Reagent not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)