# Movie Recommender System

A Streamlit-based movie recommender system that uses TMDB data and cosine similarity to suggest movies.

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vivekdevaa124/Movie-Recommender-System.git
   cd Movie-Recommender-System
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit requests pandas scikit-learn nltk
   ```

3. **Download the dataset**:
   Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the root directory.

4. **Rebuild the model**:
   Since the large `.pkl` files are not included in the repository, you need to generate them:
   ```bash
   python rebuild_model.py
   ```

5. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## Note on Posters
The app uses the TMDB API to fetch posters. If posters don't load, you can provide your own API key in the code or via the UI (if implemented).
