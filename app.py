import joblib
import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Movie Recommender System", layout="wide")


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url).json()

    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None


def recommend(movie):
    index = new_movies[new_movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity_score[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_release_dates = []

    for i in distances[1:6]:
        movie_row = new_movies.iloc[i[0]]
        movie_id = movie_row['movie_id']

        recommended_movie_names.append(movie_row['title'])
        recommended_movie_posters.append(fetch_poster(movie_id))

        if 'release_date' in new_movies.columns:
            recommended_movie_release_dates.append(movie_row['release_date'])
        else:
            recommended_movie_release_dates.append("N/A")

    return recommended_movie_posters, recommended_movie_names, recommended_movie_release_dates


def show_movie_section(movie_df, section_title):
    st.subheader(section_title)

    for start in range(0, len(movie_df), 5):
        row = movie_df.iloc[start:start+5]
        cols = st.columns(5)

        for idx, (_, movie) in enumerate(row.iterrows()):
            with cols[idx]:
                st.text(movie['title'])

                if 'release_date' in movie_df.columns:
                    st.caption(movie['release_date'])

                poster = fetch_poster(movie['movie_id'])
                if poster:
                    st.image(poster)
                else:
                    st.write("Poster not available")


st.header('Movie Recommender System')

new_movies = pd.read_csv('new_movies.csv')
pop_movies = pd.read_csv('pop_movies.csv')
similarity_score = joblib.load('similarity.joblib')

movie_list = new_movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

show_recommendations = st.button('Show Recommendation')

if show_recommendations:
    recommended_movie_posters, recommended_movie_names, recommended_movie_release_dates = recommend(selected_movie)

    st.subheader(f"Recommended Movies for {selected_movie}")

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            st.text(recommended_movie_names[i])
            st.caption(recommended_movie_release_dates[i])

            if recommended_movie_posters[i]:
                st.image(recommended_movie_posters[i])
            else:
                st.write("Poster not available")
else:
    show_movie_section(pop_movies.head(50), "Top 50 Popular Movies")