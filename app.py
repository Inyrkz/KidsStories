'''runnig flask app'''
import pickle
import json
import flask
from flask import Flask, jsonify, request
from ks2 import user_age


#load model
MODEL = pickle.load(open('MODEL.pkl', 'rb'))

#app
app = Flask(__name__)

#routes
@app.route('/', methods=['POST'])
def predict():
    '''function to predict'''
    data = request.get_json(force=True)
    #convert json to dictionary
    data = json.loads(data)
    #get int value from the 'Age' key in the dictionary
    age = int(data['Age'])
    output = user_age(age)
    #COnvet dataframe to dictionary
    output = output.set_index('Title').T.to_dict('list')
    #CONVERT dict to json
    #result = json.dumps(INFO)
    result = jsonify(output)
    output = {'results': result[0]}
    return output
    #INFO datafram will be converted to json
    #INFO = INFO.to_json(orient='records')
   #get data
    #MY_AGE = request.get_json(force=True)
    #convert data into dataframe
    #data.update((x, [y]) for x, y in data.items())
    #data_df = pd.DataFrame.from_dict(data)
    #predictions
    #result = MODEL(data_df)
    #send back to browser
    #output = {'results': int(result[0])}
    #return data
    #return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
    