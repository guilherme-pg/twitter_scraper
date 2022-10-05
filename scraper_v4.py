# SCRAPER version 4.0

# WORKING PERFECTLY


import snscrape.modules.twitter as sntwitter
import pandas as pd


# query = "(from:SOMEONE) until:YEAR-MONTH-DAY since:YEAR-MONTH-DAY"
query = "(from:SOMEONE) until:2022-10-05 since:2022-01-01"
tweets = []
limit = 3000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username,
                       tweet.content])


df = pd.DataFrame(tweets, columns=["date", "user", "tweet"])





