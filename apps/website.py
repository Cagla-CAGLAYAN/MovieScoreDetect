import streamlit as st
from PIL import Image
import requests
from io import BytesIO


def st_vertical_space(n):
    for i in range(n):
        st.write(" ") 
        
        
movies_drama = {
    "Joker":{"image_url":"https://m.media-amazon.com/images/M/MV5BYTkyM2JlNjctMmJiOC00ZTZiLWFlNjQtOTMwMjlhNDliZGIwXkEyXkFqcGc@._V1_QL75_UX147_.jpg",
                    "movie_url":"https://www.imdb.com/title/tt11315808/?ref_=sr_t_4"
                    },
    "Speak No Evi":{"image_url":"https://m.media-amazon.com/images/M/MV5BMWI2OWFjNjgtOTQ2Zi00MjlmLTg2MGYtNmE4MjMyZjIzMDA0XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
              "movie_url":"https://www.imdb.com/title/tt27534307/?ref_=sr_t_5"
              },
    "Thunderbolts":{"image_url":"https://m.media-amazon.com/images/M/MV5BYTVlNDViYWUtYmQ4Ny00Y2NhLWFjMGMtNTEyYTg5ZWNkMzhiXkEyXkFqcGc@._V1_.jpg",
              "movie_url":"https://www.imdb.com/title/tt20969586/?ref_=sr_t_2"
              },
    "Megalopolis":{"image_url":"https://m.media-amazon.com/images/M/MV5BOTQ2MTcwODgtOTg3Yi00M2RmLWEyMDQtY2IzZmRlYzM3YzhjXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
              "movie_url":"https://www.imdb.com/title/tt10128846/?ref_=sr_t_3"
             },
    "The Substance":{"image_url":"https://m.media-amazon.com/images/M/MV5BZDQ1NGE5MGMtYzdlZC00ODExLWJlMDMtNWU4NjA5OWYwMDEwXkEyXkFqcGc@._V1_QL75_UY133_CR1,0,90,133_.jpg",
              "movie_url":"https://www.imdb.com/title/tt17526714/?ref_=sr_t_1"
              }

}

movies_comedy = {
    "Beetlejuice": {"image_url":"https://m.media-amazon.com/images/M/MV5BYjkwNzVlNDEtMTJlNy00OTdlLTljYWItM2RkZmZkYzY3YjM2XkEyXkFqcGc@._V1_.jpg",
                    "movie_url":"https://www.imdb.com/title/tt0094721/?ref_=sr_t_3"
                    },
    "Inside Out 2": {"image_url":"https://m.media-amazon.com/images/M/MV5BYWY3MDE2Y2UtOTE3Zi00MGUzLTg2MTItZjE1ZWVkMGVlODRmXkEyXkFqcGc@._V1_QL75_UX190_CR0,0,190,281_.jpg",
                     "movie_url":"https://www.imdb.com/title/tt22022452/?ref_=sr_t_2"
                     },
    "Deadpool & Wolverine": {"image_url": "https://m.media-amazon.com/images/M/MV5BZTk5ODY0MmQtMzA3Ni00NGY1LThiYzItZThiNjFiNDM4MTM3XkEyXkFqcGc@._V1_.jpg",
                             "movie_url": "https://www.imdb.com/title/tt6263850/?ref_=sr_t_4"
                    },
    "Am I Racist?": {"image_url": "https://m.media-amazon.com/images/M/MV5BZTI3YWExY2YtNDQ0NC00ZDEwLThmMzktOTRjMjE1YWQ0YWFhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                     "movie_url": "https://www.imdb.com/title/tt33034103/?ref_=sr_t_5"
                     },
    "Red One" : {"image_url": "https://m.media-amazon.com/images/M/MV5BN2JhM2UwMjItYzNlMC00YjhjLWJjYjUtZWI1NDMxZmMyN2YzXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                 "movie_url": "https://www.imdb.com/title/tt14948432/?ref_=sr_t_6"
                 }
                 }



movies_crime = {
    "Wolfs": {"image_url": "https://m.media-amazon.com/images/M/MV5BNWI2MzdiM2ItMTg2Zi00MTYwLThlZmItM2FkNWI4NjE3ZjRhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
              "movie_url": "https://www.imdb.com/title/tt14257582/?ref_=sr_t_2"
              },
    "Rebel Ridge": {"image_url": "https://m.media-amazon.com/images/M/MV5BYTE4ZDE5ZTktZWZkMC00MGY4LWFkZDUtZTc5YWU3NzM2YmM3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
              "movie_url": "https://www.imdb.com/title/tt11301886/?ref_=sr_t_4"
              },
    "The Batman": {"image_url": "https://m.media-amazon.com/images/M/MV5BMmU5NGJlMzAtMGNmOC00YjJjLTgyMzUtNjAyYmE4Njg5YWMyXkEyXkFqcGc@._V1_.jpg",
              "movie_url": "https://www.imdb.com/title/tt1877830/?ref_=sr_t_5"
              },
    "Killer Heat": {"image_url": "https://m.media-amazon.com/images/M/MV5BYmI2MzhmZmEtZjMyZC00MzJiLTlkZTEtNGNhZDEwYWVmMWZhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
              "movie_url": "https://www.imdb.com/title/tt27419292/?ref_=sr_t_6"
              },
    "Longlegs": {"image_url": "https://m.media-amazon.com/images/M/MV5BNDQxZjM3YjYtZjI1MC00Y2U3LTllM2ItYjFiZmNiNTJjOTk0XkEyXkFqcGc@._V1_.jpg",
              "movie_url": "https://www.imdb.com/title/tt23468450/?ref_=sr_t_7"
              }
    
}
        
with st.container():
    col1, col2 = st.columns([5,1]) 

    with col1:
        selected = st.text_input("", "Search...")

    with col2:
        st_vertical_space(2)
        button_clicked = st.button("OK")
        
    

total_movie_count = len(movies_drama)
counter = 0
limit = 5

movie_rows = st.columns(limit)
st.write("Drama")
with st.container(border = True):
    
    for movie_name, movie_info in movies_drama.items():
        if counter % limit  == 0:
            movie_rows = st.columns(limit)
        image_url = movie_info["image_url"]
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img_resized = img.resize((64, 64) )
        with movie_rows[counter]:
            st.markdown(
                    f'<a href="{movie_info["movie_url"]}" target="_blank"><img src="{image_url}" width="128"></a>',
                    unsafe_allow_html=True,
            )                        
        if counter == limit-1:
            counter = 0
            movie_columns = st.columns(limit)
        else:
            counter += 1

st.write("Comedy")
with st.container(border = True):
    for movie_name, movie_info in movies_comedy.items():
        if counter % limit  == 0:
            movie_rows = st.columns(limit)
        image_url = movie_info["image_url"]
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img_resized = img.resize((64, 64) )
        with movie_rows[counter]:
            st.markdown(
                    f'<a href="{movie_info["movie_url"]}" target="_blank"><img src="{image_url}" width="128"></a>',
                    unsafe_allow_html=True,
            )                        
        if counter == limit-1:
            counter = 0
            movie_columns = st.columns(limit)
        else:
            counter += 1
            
            
            
st.write("Crime")
with st.container(border = True):
    for movie_name, movie_info in movies_crime.items():
        if counter % limit  == 0:
            movie_rows = st.columns(limit)
        image_url = movie_info["image_url"]
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img_resized = img.resize((64, 64) )
        with movie_rows[counter]:
            st.markdown(
                    f'<a href="{movie_info["movie_url"]}" target="_blank"><img src="{image_url}" width="128"></a>',
                    unsafe_allow_html=True,
            )                        
        if counter == limit-1:
            counter = 0
            movie_columns = st.columns(limit)
        else:
            counter += 1
