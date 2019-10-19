'''runnig flask app'''
import pickle
import pandas as pd
from flask import Flask, jsonify, request
#from k_tories import MY_AGE, INFO, AGE_INT, STORIES, BOOKS, LENGTH
from ks2 import user_age
import json

#load model
MODEL = pickle.load(open('MODEL.pkl', 'rb'))

#app
app = Flask(__name__)
#json form
MY_AGE = {'Age':10}

#routes
@app.route('/', methods=['GET'])
def predict():
    '''function to predict'''
    return user_age(MY_AGE['Age'])
    #converts the json to python dictionary    
    #MY_AGE = json.loads(MY_AGE)  
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
    
'''    
import json
f = open('data.json')
data = json.load(f)
f.close()'''