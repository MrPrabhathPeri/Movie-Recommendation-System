import pickle
import streamlit as st
import requests
import time
time.sleep(0.5)  # wait 500ms between calls

st.markdown(
    """
    <style>
    .stApp {
        background-color: #e6f2ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Dark border for dropdown/selectbox */
    div[data-baseweb="select"] > div {
        border: 2px solid #222222 !important;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    for attempt in range(6):  # Retry up to 3 times
        try:
            url = (
                f"https://api.themoviedb.org/3/movie/{movie_id}"
                f"?api_key=a1f2ea95cdcfd24bbf351c2d16af2cfa"
                f"&language=en-US&append_to_response=images"
                f"&include_image_language=en,null"
            )
            response = requests.get(url, timeout=3)
            response.raise_for_status()
            data = response.json()

            poster_path = data.get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
            else:
                return "https://via.placeholder.com/300x450?text=No+Poster"

        except requests.exceptions.RequestException as e:
            print(f"[Attempt {attempt + 1}] Failed to fetch poster for ID {movie_id}: {e}")
            time.sleep(0.3)  # brief pause before retry

    # Final fallback after retries
    return "https://via.placeholder.com/300x450?text=Error"





from concurrent.futures import ThreadPoolExecutor

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:11]]
    movie_ids = [movies.iloc[i[0]].movie_id for i in distances[1:11]]

    with ThreadPoolExecutor(max_workers=5) as executor:
        recommended_movie_posters = list(executor.map(fetch_poster, movie_ids))

    return recommended_movie_names, recommended_movie_posters





st.header('Movie Recommender System')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    # First row
    cols_row1 = st.columns(5)
    for i in range(5):
        with cols_row1[i]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])

    # Second row
    cols_row2 = st.columns(5)
    for i in range(5, 10):
        with cols_row2[i - 5]:
            st.text(recommended_movie_names[i])
            st.image(recommended_movie_posters[i])


