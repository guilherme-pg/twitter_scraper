# SCRAPER version 2.0 with TWITTER API

#

import tweepy as tw
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

api_key_secret = os.getenv('API_KEY_SECRET')

bearer_token = os.getenv('BEARER_TOKEN ')



tweets = tweepy.Cursor(api.search, q=search_words, since=date_since).items(340)
