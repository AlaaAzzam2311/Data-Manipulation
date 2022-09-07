import pandas as pd
pd.set_option('max_rows', 5)
from learntools.core import binder; binder.bind(globals())
from learntools.pandas.creating_reading_and_writing import *
print("Setup complete.")
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])
fruits
fruit_sales = pd.DataFrame([[35, 21],[41,34]], columns=['Apples', 'Bananas'], index=['2017 Sales','2018 Sales'])
fruit_sales
quantities = ['4 cups','1 cup','2 large','1 can']
items = ['Flour','Milk','Eggs','Spam']
ingredients = pd.Series(quantities,index=items,name='Dinner')
review = '../input/wine-reviews/winemag-data_first150k.csv'
reviews = pd.read_csv(review, index_col = 0)
reviews
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals
animals.to_csv('cows_and_goats.csv')
