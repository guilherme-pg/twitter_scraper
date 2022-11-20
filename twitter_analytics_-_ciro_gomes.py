# Ciro Analytics

# TO IMPROVE: separate responsibilities


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import seaborn as sns


df = pd.read_excel(r'df_tweets.xlsx')


# separate dates and time ???????????????????????? require?
df['dates'] = pd.to_datetime(df['date']).dt.date
df['time'] = pd.to_datetime(df['date']).dt.time




df['n_tweet'] = 1

df['date'] = pd.to_datetime(df['date'])


tweets_by_day = df.resample('D', on='date')['n_tweet'].sum()
tweets_by_week = df.resample('W', on='date')['n_tweet'].mean() # REQUIRE: SET MEAN
tweets_by_month = df.resample('M', on='date')['n_tweet'].sum()


tweets_by_day = tweets_by_day.to_frame()
tweets_by_week = tweets_by_week.to_frame()
tweets_by_month = tweets_by_month.to_frame()


sns.lineplot(
    data=tweets_by_day,
    x= 'date',
    y= 'n_tweet'
    )


sns.lineplot(
    data=tweets_by_week,
    x= 'date',
    y= 'n_tweet',
    color='red'
    ).set(title='Tweets by day')


sns.lineplot(
    data=tweets_by_month,
    x= 'date',
    y= 'n_tweet',
    color="green"
    )


plt.xticks(rotation=45)
plt.ylabel("Number of Tweets")
plt.xlabel("")
# change months to initials
# set line with avarenge
# set margin ?


# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

# SAVE PLOT
#plt.savefig("twitter_analytic_ciro_gomes_tweets_by_day.jpg")









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
        df_both_candidates['candidate'] = "Bolsonaro and Lula"

    elif "lula" in row['tweet']:
        df_lula.loc[len(df_lula.index)] = row
        df_lula['candidate'] = "Lula"
    
    elif "bolsonaro" in row['tweet']:
        df_bolsonaro.loc[len(df_bolsonaro.index)] = row
        df_bolsonaro['candidate'] = "Bolsonaro"
    
    elif "ciro" in row['tweet']:
        df_ciro.loc[len(df_ciro.index)] = row
        df_ciro['candidate'] = "Ciro"


df_candidates = pd.concat([df_both_candidates,
          df_lula,
          df_bolsonaro,
          df_ciro],
          ignore_index=True)

    
def to_plot(df, ylimit, title):
    
    # TO IMPROVE: change x and y varaibles structure
    
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)
    
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
    
    fig.suptitle(title, fontsize=16)  # TO IMPROVE
    fig.autofmt_xdate()
    
    if ylimit == 28000:
        for ax in axs.flat:
            ax.set_xlim([datetime.date(2022, 8, 31), datetime.date(2022, 10, 3)])
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%d'))
            ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
            
    else:    
        for ax in axs.flat:
            ax.set_xlim([datetime.date(2021, 12, 20), datetime.date(2022, 10, 30)])
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
            ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    
    plt.setp(axs, ylim=(0, ylimit))
    plt.tight_layout()
        




# GENERAL PLOT
ylimit = 50000
title = 'Likes by mentions'
to_plot(df, ylimit, title)

plt.savefig("twitter_analytic_election_ciro_gomes_likes_by_mentions_with_outlier.jpg")
        




# WITHOUT OUTLIER
df_withoutlier = df.loc[df['likes'] < 40000]

ylimit = 32000
title = 'Likes by mentions without the outlier'
to_plot(df_withoutlier, ylimit, title)

plt.savefig("twitter_analytic_election_ciro_gomes_likes_by_mentions.jpg")
     




# ONLY OCTOBER
start_date = "2022-09-01"
end_date = "2022-10-03"

period = (df['date'] >= start_date) & (df['date'] <= end_date)
df_october = df.loc[period]

ylimit = 28000
title = 'Likes by mentions at the month before the first election round of 2022'
to_plot(df_october, ylimit, title)

plt.savefig("twitter_analytic_election_ciro_gomes_likes_by_mentions_october.jpg")






# DONUT PLOTS

# TO IMPROVE: select colors
# TO IMPROVE: set labels
# TO IMPROVE: set percents
colores = {
    "Lula":"red",
    "Bolsonaro":"blue",
    "Bolsonaro and Lula":"purple"
    }
df_without_ciro = df_candidates.loc[df_candidates['candidate'] != "Ciro"]
total_citation_candidates = df_without_ciro['candidate'].value_counts()
plt.pie(total_citation_candidates,
        wedgeprops =colores)
my_circle = plt.Circle( (0,0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(my_circle)

plt.suptitle("Amount of Citations")
plt.show()



