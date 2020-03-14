'''runnig flask app'''
import json
from flask import Flask, jsonify, request
from flask_restful import Api
from ks2 import user_age

#app
app = Flask(__name__)
api = Api(app)

#routes
@app.route('/', methods=['POST'])
def predict():
    '''function to predict'''
    #data = request.json.get('Age')
    message = request.get_json(force=True)
    #get value from the 'Age' key in the json
    age = int(message['age'])
    output = user_age(age)
    response = {
        'reply' : output
    } #sends a response to the static html page
    
    return jsonify(response) #returning a jsonified response
    #return jsonify({"Recommended Stories":output})

if __name__ == '__main__':
    app.run(debug=True)
    