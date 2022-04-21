from tkinter import Menu
import pandas as pd

df = pd.read_csv('./data/2_gleam_twitter_rank.csv')
raw1 = pd.read_csv('./files/gleam1.csv')
raw2 = pd.read_csv('./files/gleam2.csv')

# here is the random function
# df = df.sample(n=1000)

result1 = raw1[raw1['Email'].isin(df['Email'])]
result2 = raw2[raw2['Email'].isin(df['Email'])]

print(result1)
print(result2)
result = result1.merge(result2, on='Email')

menu_list = ['Name_x', 'Twitter_x', 'Discord_x', 'Country_y', 'Twitter_y', 'Details']
result[menu_list].to_csv('./result/gleam-result.csv', index=False)
