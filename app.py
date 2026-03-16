import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    try:
        url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
        data = requests.get(url, timeout=5)
        data.raise_for_status()
        data = data.json()
        poster_path = data.get('poster_path')
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
    except Exception as e:
        print(f"Error fetching poster for {movie_id}: {e}")
    
    # Fallback image if API fails or poster_path is missing
    return "https://images.unsplash.com/photo-1594908900066-3f47337549d8?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_resource
def load_data():
    if os.path.exists('movie_list.pkl'):
        movies = pickle.load(open('movie_list.pkl','rb'))
    else:
        # Fallback to CSV processing if pkl is missing (can be slow on Vercel)
        if not os.path.exists('tmdb_5000_movies.csv') or not os.path.exists('tmdb_5000_credits.csv'):
            st.error("Data files (movie_list.pkl or CSVs) are missing!")
            return None, None
        
        st.info("Generating model from CSVs... (First time only)")
        # Import the rebuild logic directly if we can't find pkl
        try:
            import rebuild_model # This will run the script on import
            movies = pickle.load(open('movie_list.pkl','rb'))
        except Exception as e:
            st.error(f"Rebuild failed: {e}")
            return None, None
            
    # Always calculate similarity in memory to avoid huge file storage
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    similarity = cosine_similarity(vectors)
    return movies, similarity

st.header('Movie Recommender System')

movies, similarity = load_data()

if movies is None or similarity is None:
    st.warning("Please ensure tmdb_5000_movies.csv and tmdb_5000_credits.csv are present.")
    st.stop()

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
