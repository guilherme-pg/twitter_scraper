# Ciro Tweets Analytics

# TO IMPROVE: separate responsibilities

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import seaborn as sns

df = pd.read_excel(r'df_tweets.xlsx')





# ~~~~~~~~~~~~~~~~~~  GENERAL ADJUSTS  ~~~~~~~~~~~~~~~~~~
df['n_tweet'] = 1

df['date'] = pd.to_datetime(df['date'])

start_date = '2022-01-01'
end_date = '2022-09-30'

df_without_october = df[df.date.between(start_date, end_date)]

tweets_by_day = df.resample('D', on='date')['n_tweet'].sum().to_frame()
tweets_by_day_without_october = df_without_october.resample('D', on='date')['n_tweet'].sum().to_frame()





# ~~~~~~~~~~~~~~~~~~  DISTRIBUTION and CENTER MEASURES  ~~~~~~~~~~~~~~~~~~
tweets_by_day_aggregated = tweets_by_day_without_october.groupby('n_tweet',
                                                 as_index=False).value_counts()

mean = tweets_by_day_aggregated['count'].mean()

val1 = tweets_by_day_aggregated[tweets_by_day_aggregated['n_tweet'] > tweets_by_day_aggregated['n_tweet'].median()].iloc[0]
val2 = tweets_by_day_aggregated[tweets_by_day_aggregated['n_tweet'] < tweets_by_day_aggregated['n_tweet'].median()].iloc[-1]

palette = ['red' if val in [val1['n_tweet'], val2['n_tweet']] 
           else 'orange'
           for val in tweets_by_day_aggregated['n_tweet']]


# TO IMPROVE: add mode
plot = sns.barplot(data=tweets_by_day_aggregated,
            x='n_tweet',
            y='count',
            palette=palette,
            alpha=.5)

plot.axhline(mean, color='grey')
plot.set(title='Median as red columns and Mean as the line')
plt.ylabel("Number of times Tweets per day")
plt.xlabel("Number of Tweets by Day")
# agregar por quantidade de postagem
# agregar pela quantidade de likes
# agregar pela quantidade de retweets
# agregar pela quantidade de comentários

plt.savefig("saved_charts/twitter_analytic_ciro_gomes_mean_median_mode.jpg",
            dpi=300)





# ~~~~~~~~~~~~~~~~~~  TWEETS BY DAY AND AVERAGE BY WEEK AND MONTH  ~~~~~~~~~~~~~~~~~~
# TO IMPROVE: CHANGE 'tweets by day' TO SCATTER PLOT
# TO IMPROVE: PLOT FROM DIFFERENT COLUMNS
# TO IMPROVE: SET MARGIN TO TITLE (BOTTOM) AND Y LABEL (RIGHT)

tweets_by_day['by_week'] = tweets_by_day['n_tweet'].rolling(7).mean()

tweets_by_day['by_month'] = tweets_by_day['n_tweet'].rolling(30).mean()
tweets_by_day = tweets_by_day.dropna()

plt.figure(figsize=(10, 6))
with sns.axes_style("whitegrid"):
    sns.scatterplot(
        data=tweets_by_day,
        x= 'date',
        y= 'n_tweet',
        color="orange",
        alpha=0.5,
        label="tweets by day"
        ).set(title='Tweets by day and average by week and month')
    
    sns.lineplot(
        data=tweets_by_day,
        x= 'date',
        y= 'by_week',
        color='blue',
        alpha=0.5,
        label="average tweets by week"
        )
    
    sns.lineplot(
        data=tweets_by_day,
        x= 'date',
        y= 'by_month',
        color="red",
        alpha=0.5,
        label="average tweets by month"
        )

plt.xticks(rotation=45)
plt.ylabel("Number of Tweets")
plt.xlabel("")

plt.savefig("saved_charts/twitter_analytic_ciro_gomes_tweets_by_day.jpg",
            dpi=300)





# ~~~~~~~~~~~~~~~~~~  ENGAGEMENT BY QUOTE  ~~~~~~~~~~~~~~~~~~
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


# TO IMPROVE: DETECT OUTLIER AND CUT IT
# TO IMPROVE: SET LINE WITH THE AVERAGE BY WEEK
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
        


# ~~~~~~~~ ENGAGEMENT GENERAL PLOT
ylimit = 50000
title = 'Likes by mentions'
to_plot(df, ylimit, title)

plt.savefig("saved_charts/twitter_analytic_ciro_gomes_likes_by_mentions_with_outlier.jpg",
            dpi=300)
        


# ~~~~~~~~ ENGAGEMENT WITHOUT OUTLIER
df_withoutlier = df.loc[df['likes'] < 40000]

ylimit = 32000
title = 'Likes by mentions without the outlier'
to_plot(df_withoutlier, ylimit, title)

plt.savefig("saved_charts/twitter_analytic_ciro_gomes_likes_by_mentions.jpg",
            dpi=300)
     



# ~~~~~~~~ ENGAGEMENT ONLY OCTOBER
start_date = "2022-09-01"
end_date = "2022-10-03"

period = (df['date'] >= start_date) & (df['date'] <= end_date)
df_october = df.loc[period]


ylimit = 28000
title = 'Likes by mentions a month before the first round of 2022 election'
to_plot(df_october, ylimit, title)

plt.savefig("saved_charts/twitter_analytic_ciro_gomes_likes_by_mentions_october.jpg",
            dpi=300)






# ~~~~~~~~~~~~~~~~~~  QUOTE BY ADVERSARY  ~~~~~~~~~~~~~~~~~~

# TO IMPROVE: select colors by dataframe values
# TO IMPROVE: set labels by dataframe values
#colores = {"Lula":"red", "Bolsonaro":"blue", "Bolsonaro and Lula":"purple"}
colores = ["blue", "purple", "red"]
labels = ["Bolsonaro", "Bolsonaro and Lula", "Lula"]

df_without_ciro = df_candidates.loc[df_candidates['candidate'] != "Ciro"]
total_citation_candidates = df_without_ciro['candidate'].value_counts()

plt.figure(figsize=(10, 6))
plt.pie(total_citation_candidates,
        colors =colores,
        labels=labels,
        autopct='%1.1f%%',
        pctdistance=.5)

my_circle = plt.Circle( (0,0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(my_circle)

plt.suptitle("Amount of Citations")

plt.savefig("saved_charts/twitter_analytic_ciro_gomes_likes_adversaries_citations.jpg",
            dpi=300)


