# Ciro Analytics


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime



df = pd.read_excel(r'df_tweets.xlsx')



# convert tweet to lower case
df['tweet'] = df['tweet'].str.lower()


column_names = ["date", "user", "tweet", "hashtags", 
                "retweets", "replys", "likes", "quotes"]



df_both_candidates = pd.DataFrame(columns=column_names)
df_bolsonaro = pd.DataFrame(columns=column_names)
df_lula = pd.DataFrame(columns=column_names)
df_ciro = pd.DataFrame(columns=column_names)




for index, row in df.iterrows():
    
    if ("lula" in row['tweet']) and ("bolsonaro" in row['tweet']):
        df_both_candidates.loc[len(df_both_candidates.index)] = row

    elif "lula" in row['tweet']:
        df_lula.loc[len(df_lula.index)] = row
    
    elif "bolsonaro" in row['tweet']:
        df_bolsonaro.loc[len(df_bolsonaro.index)] = row
    
    elif "ciro" in row['tweet']:
        df_ciro.loc[len(df_ciro.index)] = row





fig, axs = plt.subplots(2,2)

x = df_bolsonaro['date']
y = df_bolsonaro['likes']
axs[0, 0].scatter(x, y, color='blue', alpha=0.5, marker=".", s=20)
axs[0, 0].set_title('Bolsonaro')

x = df_lula['date']
y = df_lula['likes']
axs[0, 1].scatter(x, y, color='red', alpha=0.5, marker=".", s=20)
axs[0, 1].set_title('Lula')

x = df_both_candidates['date']
y = df_both_candidates['likes']
axs[1, 0].scatter(x, y, color='green', alpha=0.5, marker=".", s=20)
axs[1, 0].set_title('Bolsonaro and Lula')

x = df_ciro['date']
y = df_ciro['likes']
axs[1, 1].scatter(x, y, color='pink', alpha=0.5, marker=".", s=20)
axs[1, 1].set_title('Ciro')

fig.suptitle('Likes by mentions', fontsize=16)
fig.tight_layout()
fig.autofmt_xdate()
for ax in axs.flat:
    ax.set_xlim([datetime.date(2021, 12, 20), datetime.date(2022, 10, 30)])
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))

plt.setp(axs, ylim=(0, 50000))


plt.savefig("twitter_analytic_election_ciro_gomes_likes_by_mentions.jpg")

