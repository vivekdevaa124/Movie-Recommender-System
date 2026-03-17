Movie Recommender System 🎬
A content-based recommendation engine that helps users discover their next favorite film. By analyzing movie metadata—such as genres, keywords, and cast—the system calculates similarity scores to provide highly relevant suggestions tailored to user preferences.
🚀 Overview
This project bridges the gap between massive movie databases and user discovery. Unlike collaborative filtering, which relies on other users' ratings, this Content-Based Filtering approach focuses on the attributes of the items themselves. If you like a movie with specific themes or directors, this system finds others that share those DNA traits.
<img width="1919" height="878" alt="image" src="https://github.com/user-attachments/assets/85724b47-3448-48c7-a359-e6ee4d723028" />

<img width="1902" height="892" alt="image" src="https://github.com/user-attachments/assets/61e04893-7041-4653-97dd-d727d3b2e5aa" />

🛠️ Tech Stack
Language: Python

Machine Learning: Scikit-learn (for Vectorization and Cosine Similarity)

Data Manipulation: Pandas & NumPy

Frontend/Deployment: Streamlit

Dataset: TMDB 5000 Movie Dataset (or similar)
🧠 How It WorksData Preprocessing: 
Cleaning movie metadata and combining relevant features (overview, genres, keywords, cast, and crew) into a single "tags" column.
Vectorization: Converting text tags into numerical vectors using Bag of Words or TF-IDF.
Similarity Measurement: Calculating the Cosine Similarity between vectors to find the mathematical "distance" between movies.The Cosine Similarity formula used:$$similarity = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$
Recommendation: When a user selects a movie, the system sorts the top 5–10 movies with the highest similarity scores.
💻 Getting Started
Prerequisites
Python 3.8+

Pip

✨ Features
Vectorized Search: Uses natural language processing (NLP) to find movies with similar thematic elements, not just matching genres.

Real-time Poster Fetching: Integrates with the TMDB API to display high-quality movie posters for a more immersive UI.

Interactive UI: A clean, responsive dashboard built with Streamlit for seamless user interaction.

Scalable Similarity Matrix: Efficiently handles thousands of movie records using compressed pickle files for fast retrieval.
Installation
Clone the repository:

git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
Install dependencies:

pip install -r requirements.txt
Run the application:

streamlit run app.py

🚀 Deployment
The application is configured for easy deployment on Streamlit Cloud or Heroku.

Ensure your requirements.txt includes requests, streamlit, and pickle-mixin.

Add your TMDB API Key as a secret environment variable to keep it secure.

Run the live instance:

streamlit run app.py --live

