import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")
reviews.head()
desc = reviews.description
first_description = reviews['description'][0]
first_description
first_row = reviews.iloc[0][:]
first_row
first_descriptions = reviews.iloc[0:10]['description']
first_descriptions
rows = [1,2,3,5,8]
sample_reviews = reviews.loc[rows][:]
sample_reviews
rows=[0,1,10,100]
cols = ['country','province','region_1','region_2']
df = reviews.loc[rows,cols]
df
cols=['country','variety']
df = reviews.loc[0:99,cols]
df
italian_wines = reviews[reviews.country=='Italy']
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia', 'New Zealand']))& (reviews.points >= 95)]
top_oceania_wines

