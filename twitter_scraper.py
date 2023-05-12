# SCRAPER machine

import snscrape.modules.twitter as sntwitter
import pandas as pd


def process_data(search_obj, max_tweets_numb, start_date, end_date):
    print(start_date)
    print(end_date)

    # query GUIDE = f"(from:NAME) until:YEAR-MONTH-DAY since:YEAR-MONTH-DAY"
    query = f"(from:{search_obj}) since:{start_date} until:{end_date}"

    tweets = []

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        if len(tweets) == max_tweets_numb:
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

    df['date'] = df['date'].dt.tz_localize(None)  # remove timezones

    # SAVING
    df.to_csv('dataframe/df_tweets.csv', index=False)
