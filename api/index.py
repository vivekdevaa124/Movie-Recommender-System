import os
import pickle
import pandas as pd
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Load data on startup
MOVIES_PKL = 'movie_list.pkl'

def load_data():
    if os.path.exists(MOVIES_PKL):
        movies = pickle.load(open(MOVIES_PKL, 'rb'))
        return movies
    return None

movies_df = load_data()

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url, timeout=5)
        data.raise_for_status()
        json_data = data.json()
        poster_path = json_data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except Exception as e:
        print(f"Error fetching poster for {movie_id}: {e}")
    return "https://images.unsplash.com/photo-1594908900066-3f47337549d8?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60"

def get_recommendations(movie_title):
    if movies_df is None:
        return [], []
    
    try:
        idx = movies_df[movies_df['title'] == movie_title].index[0]
        
        # Calculate similarity in memory (same logic as Streamlit app)
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(movies_df['tags']).toarray()
        similarity = cosine_similarity(vectors)
        
        distances = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
        
        names = []
        posters = []
        for i in distances[1:7]:
            m_id = movies_df.iloc[i[0]].movie_id
            names.append(movies_df.iloc[i[0]].title)
            posters.append(fetch_poster(m_id))
        return names, posters
    except Exception as e:
        print(f"Error in recommendation: {e}")
        return [], []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/movies')
def get_movies():
    if movies_df is not None:
        return jsonify(movies_df['title'].tolist())
    return jsonify([])

@app.route('/api/recommend')
def recommend():
    movie = request.args.get('movie')
    if not movie:
        return jsonify({"error": "No movie provided"}), 400
    
    names, posters = get_recommendations(movie)
    return jsonify({"names": names, "posters": posters})

# Vercel requires the app object to be named 'app'
if __name__ == '__main__':
    app.run(debug=True)
