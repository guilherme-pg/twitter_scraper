# Ciro Analytics


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(r'df_tweets.xlsx')



# convert tweet to lower case
df['tweet'] = df['tweet'].str.lower()


column_names = ["date", "user", "tweet", "hashtags", 
                "retweets", "replys", "likes", "quotes"]



df_both_candidates = pd.DataFrame(columns=column_names)
df_bolsonaro = pd.DataFrame(columns=column_names)
df_lula = pd.DataFrame(columns=column_names)





for index, row in df.iterrows():
    
    if ("lula" in row['tweet']) and ("bolsonaro" in row['tweet']):
        df_both_candidates.loc[len(df_both_candidates.index)] = row

    elif "lula" in row['tweet']:
        df_lula.loc[len(df_lula.index)] = row
    
    elif "bolsonaro" in row['tweet']:
        df_bolsonaro.loc[len(df_bolsonaro.index)] = row








x = df_both_candidates['date']
y = df_both_candidates['likes']
plt.scatter(x, y, color='green', alpha=0.5, marker=".", s=20)

x = df_bolsonaro['date']
y = df_bolsonaro['likes']
plt.scatter(x, y, color='blue', alpha=0.5, marker=".", s=20)

x = df_lula['date']
y = df_lula['likes']
plt.scatter(x, y, color='red', alpha=0.5, marker=".", s=20)

plt.show()


df_lula.scatter(x='date', y='likes', label = "line 1", )
df_bolsonaro.scatter(x='date', y='likes', label = "line 2")









