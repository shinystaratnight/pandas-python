import pandas as pd
import requests


# Function to return title
def imdb_id_title(imdb_id, api_key = '42d8413'):
    imdb_id = imdb_id
    omdb_response = requests.get('http://omdbapi.com/?i='+imdb_id+'&apikey=42d8413')
    omdb_response_json = omdb_response.json()
    return omdb_response_json['Title']

# Import Data
df = pd.read_csv('df.csv')


df_most_popular = df.groupby('imdb_id')[['ip']].count().sort_values('ip', ascending = False).head(10)


# For loop to write in returned title from imdb_id_title function
df_most_popular = df_most_popular.reset_index()

for i in df_most_popular.index:
    df_most_popular.at[i, 'title'] = imdb_id_title(df_most_popular.loc[i]['imdb_id'])

print(df_most_popular.at[3, 'title'])
df_most_popular.set_index('title', inplace = True)


# Alternative methods to the above for loop?
# 1) lambda
# 2) .apply()


