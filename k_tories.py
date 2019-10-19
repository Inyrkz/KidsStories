'''
Building a popularity recommender system for kid's stories based on age
'''
#Importing Libraries
import pickle
import pandas as pd
#import numpy as np

print('----------------------------')
print('Age Ranges from 0 - 13 years')
AGE = int(input('Please enter age:'))
MY_AGE = {'Age': AGE}
if MY_AGE['Age'] > 13:
    MES = 'Age over expected range'
    print(MES)
else:
    AGE_INT = pd.read_csv(r'C:\Users\AFFIA\Desktop\Age_interaction.csv', encoding = 'latin-1')
    STORIES = pd.read_csv(r'C:\Users\AFFIA\Desktop\Kidstories.csv', encoding = 'latin-1')
    #Let's preview the first few rows of the data
    #print(STORIES.head())
    #AGE_INTERACTIONS.head()
    #Getting recommendation based on age of user
    BOOKS = AGE_INT.loc[AGE_INT.Age == MY_AGE['Age'], :].sort_values('Book_ID', ascending = False)
    LENGTH = len(AGE_INT.loc[AGE_INT.Age == MY_AGE['Age'], :])
    print("There are ", LENGTH, "books available for age ", MY_AGE['Age'])
    #Getting details of books recommended for that age
    INFO = pd.merge(BOOKS, STORIES, on = 'Book_ID')
    INFO = INFO.sort_values(['Likes', 'Dislikes'], ascending=[False, True])
    INFO = INFO.loc[:, ['Title']]
    print(INFO)

pickle.dump(INFO, open("MODEL.pkl", "wb"))
