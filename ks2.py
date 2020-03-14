'''
Building a popularity recommender system for kid's stories based on age
'''
#Importing Libraries
import pandas as pd
#import numpy as np

def user_age(age):
    '''
    Function to get age of user and display books available for that age
    '''
    #Reading the dataset
    age_int = pd.read_csv('Age_interaction.csv', encoding='latin-1')
    stories = pd.read_csv('Kidstories.csv', encoding='latin-1')
    #Let's preview the first few rows of the data
    #print(STORIES.head())
    #AGE_INTERACTIONS.head()
    #Getting recommendation based on age of user
    books = age_int.loc[age_int.Age == age, :].sort_values('Book_ID', ascending=False)
    #length = len(age_int.loc[age_int.Age == age, :])
    #print("There are ", length, "books available for age ", age)
    #Getting details of books recommended for that age
    info = pd.merge(books, stories, on='Book_ID')
    info = info.sort_values(['Likes', 'Dislikes'], ascending=[False, True])
    info = info.loc[:, ['Title']]
    # info = info.to_string(index=False) #convert dataframe to string without the index
    info = info.to_dict(orient='list') #convert dataframe to dictionary conta
    if age > 13:
        ans = 'Age over expected range'
    else:
        ans = info
    return str(ans) #convert output from dictionary to string

#while True:
#Testing the data
#age = 1
#print(user_age(int(age)))
#print(type(user_age(int(age))))
