# WORD/TAG CLOUD


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv(r'df_tweets.csv')


# list_words_column = list( df_ [' column_name '] )
list_words_column = list(df['tweet'])


# EXCLUDING WORDS
exclude_words = ["a", "A", "o", "as", "os", "ao", "ante", "do", "da",
                 "dos", "das", "às", "nos", "nas", "https", "ma", "que", "Que",
                 "com", "de", "em", "para", "perante", "por", "sem", "sob",
                 "no", "na", "é", "como", "https", "pela", "pelo",
                 "já", "está", "estão", "t", "co", "uma", "um", "isso", 
                 "esse", "essa", "este", "esta", "Esta", "Este",
                 "entre", "https://T.Co", "pra", "é", "/", "|", "Da", "Do"
                 "sobre", "trás", "à", "e", ".", ";", ",", ":", ";", "-"]

exclude_http = "http"


all_words = []

for item in list_words_column:
    list_words = item.split()
    
    # convert all to lowercase
    a = (map(lambda x: x.lower(), list_words))
    list_words = list(a)
    
    # exclude http links
    list_words = [item for item in list_words if not item.startswith(exclude_http)]

    # exclude words
    # TO IMPROVE: some words that shouldn't appear are appearing: O, Que
    for element in list_words:
        if element in exclude_words:
            list_words.remove(element)
    
    # convert all to title case
    a = (map(lambda x: x.title(), list_words))
    list_words = list(a)
    
    all_words = all_words + list_words

type(all_words[82])  # change 82 to 100, 75 or 50?


# CREATING THE WORD CLOUD
cloud = WordCloud(
    max_words=75,
    background_color="white",
    width=800,
    height=600
    ).generate(" ".join(all_words))


# PLOT
plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()

plt.savefig("saved_charts/twitter_analytic_words_cloud.jpg", dpi=300)

# TO IMPROVE: some letters and words keep appearing even though they are on the excluded list
