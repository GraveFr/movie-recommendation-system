import streamlit as st
from recommender import recommend, new_df

st.title("Movie Recommendation System")

movie_list = new_df["title"].values

selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(movie)