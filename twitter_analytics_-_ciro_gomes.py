# Ciro Analytics


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel(r'df_tweets.xlsx')



# convert tweet to lower case
df['tweet'] = df['tweet'].str.lower()


column_names = ['date', 'user', 'tweet']


df_both_candidates = pd.DataFrame(columns=column_names)
df_bolsonaro = pd.DataFrame(columns=column_names)
df_lula = pd.DataFrame(columns=column_names)



# df_both_candidates = df['tweet'].str.contains('lula|bolsonaro', case=False, regex=True)
# df_lula = df['tweet'].str.contains('lula', case=False, regex=True)
# df_bolsonaro = df['tweet'].str.contains('bolsonaro', case=False, regex=True)





for index, row in df.iterrows():
    
    if ("lula" in row['tweet']) and ("bolsonaro" in row['tweet']):
    # if row['tweet'].isin(['lula', 'bolsonaro']):
    # if row['tweet'].str.contains('lula|bolsonaro', case=False, regex=True):
        df_both_candidates.loc[len(df_both_candidates.index)] = row

    elif "lula" in row['tweet']:
    # elif row['tweet'].str.contains('lula', case=False, regex=True):
        df_lula.loc[len(df_lula.index)] = row
    
    elif "bolsonaro" in row['tweet']:
    # elif row['tweet'].str.contains('bolsonaro', case=False, regex=True):
        df_bolsonaro.loc[len(df_bolsonaro.index)] = row















