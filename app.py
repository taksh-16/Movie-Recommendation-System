import streamlit as st
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie data
movies = pickle.load(open("movies.pkl", "rb"))

# Instead of loading similarity.pkl, I am creating the similarity matrix here.
# The similarity file was too large to upload to GitHub, so I regenerate it
# from the movie tags whenever the application starts.

tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
tfidf_matrix = tfidf.fit_transform(movies["clean_text"])

similarity = cosine_similarity(tfidf_matrix)


# Recommendation function
def recommend(movie_name, top_n=5):

    movie_index = movies[movies["title"] == movie_name].index[0]
    similarity_scores = list(enumerate(similarity[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_movies = []

    for movie in similarity_scores[1:top_n + 1]:
        recommended_movies.append(movies.iloc[movie[0]]["title"])

    return recommended_movies


# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Top 5 Recommended Movies")

    for movie in recommendations:
        st.write(movie)
