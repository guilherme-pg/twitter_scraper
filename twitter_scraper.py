# SCRAPER version 4.0

# WORKING PERFECTLY


import snscrape.modules.twitter as sntwitter
import pandas as pd


NAME = ""
START_DATA = ""
END_DATA = ""
NUMB_TWEETS_LIMITS = 0

# query GUIDE = f"(from:NAME) until:YEAR-MONTH-DAY since:YEAR-MONTH-DAY"
query_1 = f"(from:NAME) until:YEAR-MONTH-DAY since:YEAR-MONTH-DAY"
query = "(from:cirogomes) until:2022-10-30 since:2022-01-01"
tweets = []
limit = 10000  # NUMB_TWEETS_LIMITS

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, 
                       tweet.user.username,
                       tweet.content,
                       tweet.hashtags,
                       tweet.retweetCount,
                       tweet.replyCount,
                       tweet.likeCount,
                       tweet.quoteCount
                       ])


df = pd.DataFrame(tweets, columns=["date", "user", "tweet", "hashtags", 
                                   "retweets", "replys", "likes", "quotes"])


# remove timezones
df['date'] = df['date'].dt.tz_localize(None)


# SAVE AS EXCEL
df.to_excel('df_tweets.xlsx', index=False)



