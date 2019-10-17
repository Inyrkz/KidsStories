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
    if age > 13:
        print('Age over expected range')
    else:
        #Reading the dataset
        age_int = pd.read_csv(r'C:\Users\AFFIA\Desktop\Age_interaction.csv', encoding = 'latin-1')
        stories = pd.read_csv(r'C:\Users\AFFIA\Desktop\Kidstories.csv', encoding = 'latin-1')
        #Let's preview the first few rows of the data
        #print(STORIES.head())
        #AGE_INTERACTIONS.head()
        #Getting recommendation based on age of user
        books = age_int.loc[age_int.Age == age, :].sort_values('Book_ID', ascending = False)
        length = len(age_int.loc[age_int.Age == age, :])
        print("There are ", length, "books available for age ", age)
        #Getting details of books recommended for that age
        info = pd.merge(books, stories, on = 'Book_ID')
        info = info.loc[:, ['Book_ID', 'Title', 'Category', 'Age_range']]
        print(info)

while True:
    print('----------------------------')
    print('Age Ranges from 0 - 13 years')
    MY_AGE = int(input('Please enter age:'))
    user_age(MY_AGE)
    