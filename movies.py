# -*- coding: utf-8 -*-
"""movies.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nIhkVBWtQPrRkhKiBjV1QXnB-1XNTxnw
"""

import pandas as pd
import numpy as np

"""Upload the /content/movies_metadata.csv"""

df = pd.read_csv('/content/movies_metadata.csv').dropna(axis=1, how='all')
print(df)
df.head()

df.shape

df.columns

"""Create a variable called budget_df that contains all columns for the movies whose budget was over a million dollars."""

budget_df = df[df['budget'] > 1000000]
print(budget_df)

len(budget_df)

"""Create a Series object called budget_lookup such that you are able to use a call to budget_lookup['Dead Presidents'] to find the budget of that movie. budget_lookup = []
budget_lookup['Dead Presidents']
"""

budget_lookup = pd.Series(budget_df['budget'].values, index=budget_df['original_title'])
budget_lookup['Dead Presidents']

"""I have figured out that the first (alphabetically) movie whose title starts with an “A” is “A Bag of Hammers” and the last movie that starts with a “B” is “Byzantium”.

budget_lookup[budget_lookup.index.str.startswith('A')].sort_index()[[0]]
title
A Bag of Hammers    2000000
dtype: int64
budget_lookup[budget_lookup.index.str.startswith('B')].sort_index()[[-1]]
title
Byzantium    10000000
dtype: int64
Use that knowledge to create a series that contains budget informations for all the movies that start with an “A” or a “B”. Hint: No need to use startswith like I did above, just use the movie titles to do a slice.

budget_lookup_as_and_bs = []
budget_lookup_as_and_bs.shape

Q-3: How many movies with a budget of over a million dollars and whose title starts with an “A” or a “B” are there?
"""

budgets_as_and_bs = budget_lookup[(budget_lookup.index.str.startswith('A')) | (budget_lookup.index.str.startswith('B'))]
print(budgets_as_and_bs)
len(budgets_as_and_bs)