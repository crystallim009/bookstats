# link authors id to author name
# for books with more than one author, only the first author will be included; the rest of the authors will be deleted

import pandas as pd
import re

df1 = pd.read_csv("biography.csv")
df1 = df1.assign(authors=df1.authors.str.split(',')).explode('authors')
df1['authors'] = df1['authors'].str.strip('[]')
df1 = df1.drop_duplicates('id', keep='last') # remove duplicates from books with more than one authors

df2 = pd.read_csv("authors.csv")
df2['author_id'] = df2['author_id'].astype(str)
df0 = df1.merge(df2, how='inner', left_on='authors', right_on='author_id') # merge author id for both df and include author name into the df1
df0 = df0.drop(columns=['authors'])

df3 = pd.read_csv("categories.csv")
df0 = df0.merge(df3, how='inner', left_on='categories', right_on='category_id')
df0 = df0.drop(columns=['categories'])
df0.to_csv(r"C:\Users\thous\OneDrive\Desktop\bdepo\biography2.csv", encoding='utf-8', index=False)
