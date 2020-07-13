

import pandas as pd
import re

df = pd.read_csv("bdepo_.csv")

df = df.assign(categories=df.categories.str.split(',')).explode('categories') # split list contained in a single cell of csv file into multiple rows
df['categories'] = df['categories'].str.strip('[]') # remove the [] bracket from cells

df.to_csv(r"C:\Users\thous\OneDrive\Desktop\bdepo\bdepo_bio.csv", encoding='utf-8', index=False)
