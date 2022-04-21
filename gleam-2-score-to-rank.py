import pandas as pd

df = pd.read_csv('./data/1_gleam_twitter_score.csv')
df = df[['Email', 'usernames', 'display_scores_universal_overall']]
df.sort_values('display_scores_universal_overall', inplace=True)
df = df[df['display_scores_universal_overall'].lt(3)]

print(df)

df.to_csv('./data/2_gleam_twitter_rank.csv')
