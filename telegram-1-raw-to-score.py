from cmath import nan
import pandas as pd

df = pd.read_csv('./data/0_telegram_twitter_score_raw.csv')
df = df.replace(to_replace=r'\-', value=nan, regex=True)
df = df.dropna(subset=['user_id', 'raw_scores_universal_astroturf', 'raw_scores_universal_fake_follower'])

print(df)
df.to_csv('./data/1_telegram_twitter_score.csv')
