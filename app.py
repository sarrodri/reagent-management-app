from flask import Flask, jsonify
import json

# This is where we will make the API using Flask and Python
# Docs: https://flask.palletsprojects.com/en/3.0.x/
#Whoever works on this will need to run "pip install flask" in the command line
# use comments please n thank youuuuuuuuuuu <3

app = Flask(__name__)

# possibly use forms to intake info or engineers have data for us to import?
dummy_data = [ { 'id': 1, 'name': 'Sarah' }, { 'id': 2, 'name': 'Megan' }, { 'id': 3, 'name': 'Aly' }]


@app.route('/dummy_data', methods = ["GET"])
def index():
    return jsonify(dummy_data)

if __name__ == '__main__':
    app.run(debug=True)