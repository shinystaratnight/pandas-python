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

df_most_popular = df_most_popular.reset_index()

# Instead of for-loop, lambda take its place.
df_most_popular['title'] = list(map(lambda i: imdb_id_title(df_most_popular.loc[i]['imdb_id']), df_most_popular.index))

df_most_popular.set_index('title', inplace = True)
