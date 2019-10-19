'''runnig flask app'''
import pickle
import json
import pandas as pd
from flask import Flask, jsonify, request
#from k_tories import MY_AGE, INFO, AGE_INT, STORIES, BOOKS, LENGTH
#from ks2 import user_age


#load model
MODEL = pickle.load(open('MODEL.pkl', 'rb'))

#app
app = Flask(__name__)

#routes
@app.route('/', methods=['POST'])
def predict():
    '''function to predict'''
    age_int = pd.read_csv(r'C:\Users\AFFIA\Desktop\Age_interaction.csv', encoding = 'latin-1')
    stories = pd.read_csv(r'C:\Users\AFFIA\Desktop\Kidstories.csv', encoding = 'latin-1')
    data = request.get_json(force=True)
    data = json.loads(data)
    age = data['Age']
    books = AGE_INT.loc[age_int.Age == age, :].sort_values('Book_ID', ascending = False)
    info = pd.merge(books, stories, on = 'Book_ID')
    info = info.sort_values(['Likes', 'Dislikes'], ascending=[False, True])
    info = info.loc[:, ['Title']]
    #COnvet dataframe to dictionary
    info = info.set_index('Title').T.to_dict('list')
    #CONVERT dict to json
    #result = json.dumps(INFO)
    result = jsonify(info)
    return result
    # return user_age(MY_AGE['Age'])
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
    