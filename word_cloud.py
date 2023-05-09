# WORD/TAG CLOUD


# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_excel(r'df_tweets.xlsx')


# lista_palavras_coluna = list( df_ [' column_name '] )
lista_palavras_coluna = list( df['tweet'] )


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


todas_palavras = []

for item in lista_palavras_coluna:
    lista_palavras = item.split()
    
    # convert all to lowercase
    a = (map(lambda x: x.lower(), lista_palavras))
    lista_palavras = list(a)
    
    # exclude http links
    lista_palavras = [item for item in lista_palavras if not item.startswith(exclude_http)]

    # exclude words
    # TO IMPROVE: some words that shouldn't appear are appearing: O, Que
    for element in lista_palavras:
        if element in exclude_words:
            lista_palavras.remove(element)
    
    # convert all to title case
    a = (map(lambda x: x.title(), lista_palavras))
    lista_palavras = list(a)
    
    todas_palavras = todas_palavras + lista_palavras

type(todas_palavras[82])


# CREATING THE WORD CLOUD
cloud = WordCloud(
    max_words=75,
    background_color= "white",
    width=800,
    height=600
    ).generate(" ".join(todas_palavras))


# PLOT
plt.imshow(cloud, interpolation='bilinear' )
plt.axis('off')
plt.show()


# TO IMPROVE: some letters and words keep appearing even though they are on the excluded list
