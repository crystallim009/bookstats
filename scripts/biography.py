# extract data that belongs to category of biography;
# go to category column, search each row for '213'; if no 213 in the row, delete entire row.

import pandas as pd

df = pd.read_csv("bdepo_bio.csv")
cat=['213', '218', '216', '214', '220', '222', '230', '224', '228', '226'] # numbers for biography and its sub-categories
df = df[df['categories'].isin(cat)] # remove rows whose category does not contain any from this 'cat' list
df = df.drop_duplicates('id', keep='last')

df.to_csv(r"C:\Users\thous\OneDrive\Desktop\bdepo\biography.csv", encoding='utf-8', index=False)

# link authors key ana value
# remove duplicate titles?
