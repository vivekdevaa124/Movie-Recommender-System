import pandas as pd
import requests

def test_api(movie_title, api_key):
    try:
        movies = pd.read_csv('tmdb_5000_movies.csv')
        matches = movies[movies['title'].str.contains(movie_title, case=False, na=False)]
        if matches.empty:
            print(f"No match for '{movie_title}'")
            return
        movie = matches.iloc[0]
        movie_id = movie['id']
        title = movie['title']
        print(f"Testing for '{title}' (ID: {movie_id})")
        
        url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key)
        response = requests.get(url, timeout=10)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Poster Path: {data.get('poster_path')}")
        else:
            print(f"Error Response: {response.text}")
    except Exception as e:
        print(f"Failed: {e}")

api_key = "8265bd1679663a7ea12ac168da84d2e8"
test_api("Legend of Hercules", api_key)
test_api("Get Carter", api_key)
test_api("Avatar", api_key)
