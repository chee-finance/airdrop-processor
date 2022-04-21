from tkinter import Menu
import pandas as pd

df = pd.read_csv('./data/2_telegram_twitter_rank.csv')
raw = pd.read_csv('./files/telegram.csv', low_memory=False)

df[['user_id']] = df[['user_id']].astype(int)

# here is the random function
# df = df.sample(n=1000)


result = raw[raw['user_id'].isin(df['user_id'])]

menu_list = ['first_name', 'last_name', 'twitter', 'discord', 'wallet']
result[menu_list].to_csv('./result/telegram-result.csv', index=False)
