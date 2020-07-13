# keep columns and delete the rest

import pandas as pd

df = pd.read_csv("bdepo_orig.csv")
df = df.filter(['id', 'authors', 'bestsellers-rank', 'categories', 'lang', 'publication-date', 'rating-avg', 'rating-count', 'title'])
df.to_csv(r"C:\Users\thous\OneDrive\Desktop\bdepo\bdepo_.csv", encoding='utf-8', index=False)
