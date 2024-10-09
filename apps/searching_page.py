import streamlit as st
from PIL import Image

def st_vertical_space(n):
    for i in range(n):
        st.write(" ") 
        
def search(movies, text):
    result = []
    if len(text) > 0:
        for movie in movies:
            if text.lower() in movie["title"].lower():
                result.append(movie)
    return result


def generate_card_view(movie):

    with st.container(border = True):  
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

search_text = st.text_input("Search movies")

search_results = search(movies, search_text)
for movie in search_results:
        generate_card_view(movie)

