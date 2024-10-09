import streamlit as st
from PIL import Image
# from DB import db
# from Movie import Movie

# mydb = db()

def st_vertical_space(n):
    for i in range(n):
        st.write(" ") 
        


def generate_card_view(movie):

    with st.container(border = True):  
        if st.button("Add", key=movie["title"]):
            if "selected_movies" not in st.session_state:
                st.session_state.selected_movies = []
            st.session_state.selected_movies.append(movie["title"]) 
            st.rerun()
        cols_title = st.columns([6,1])
        with cols_title[0]:
            st.subheader(movie["title"], divider="red")
        with cols_title[1]:
            st.write(":green[" + movie["score"] + "]")

        cols = st.columns([1,3])
        with cols[0]:
            st.image(movie["image"])
        with cols[1]:
            st.write(movie["description"])
            
        

def search(movies, text):
    result = []
    if len(text) > 0:
        for movie in movies:
            if text.lower() in movie["title"].lower():
                result.append(movie)
    return result

def generate_selected_movies(selected_movies):
    for movie_title in selected_movies:
        movie = next((m for m in movies if m["title"] == movie_title), None)
        with st.container(border = True):
            if movie:
                cols_title = st.columns([1,1,1])
                with cols_title[0]:
                    st.image(movie["image"])
                with cols_title[1]:
                    st.write(movie["title"])
                with cols_title[2]:
                    if st.button("Subtract", key=f"subtract_{movie_title}"):
                        st.session_state.selected_movies.remove(movie_title)
                        st.rerun()
                        
# search_results = mydb.search(search_text)
movies = [
  {
    "title": "Movie1",
    "image": Image.open("./picture.jpg") ,
    "score": "9.9",
    "description": "The description about the first movie"
  },
 
  {
    "title": "Movie12",
    "image": Image.open("./picture.jpg") ,
    "score": "9.9",
    "description": "The description about the second movie.."
  },
  {
    "title": "Movie13",
    "image": Image.open("./picture.jpg") ,
    "score": "9.9",
    "description": "Description about the third movie third movie."
  },

  {
    "title": "Movie14",
    "image": Image.open("./picture.jpg") ,
    "score": "9.9",
    "description": "The description about about abput the fourth movie...."
  }
]


if "selected_movies" not in st.session_state:
    st.session_state.selected_movies = []

search_text = st.text_input("Search movies")

cols = st.columns(2)
with cols[0]:
    search_results = search(movies, search_text)
    for movie in search_results:
        generate_card_view(movie)

with cols[1]:
    st.write("Movies To Update")
    generate_selected_movies(st.session_state.selected_movies)
    

