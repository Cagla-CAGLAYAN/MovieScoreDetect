import streamlit as st
from PIL import Image


def st_vertical_space(n):
    for i in range(n):
        st.write(" ") 
        
        
        
with st.container():
    col1, col2 = st.columns([5,1]) 

    with col1:
        selected = st.text_input("", "Search...")

    with col2:
        st_vertical_space(2)
        button_clicked = st.button("OK")
        
    
col1, col2, col3 = st.columns([2,6,1])


with col1:
    st.image('./picture.jpg')
    container = st.container(border = True)
    container.write("place for imdb score")

    
    
with col2:
    st.markdown("<h1 style='text-align: center; color: black;'>Movie Title</h1>", unsafe_allow_html=True)
    container2 = st.container(border = True)
    container2.write("movie desciption movie desciption movie desciption movie desciption movie desciption movie desciption movie desciption movie desciption movie desciption movie desciption movie desciption movie desciption")
    container3 = st.container(border= True)
    container3.write("category1, category2, category3")
    with st.container(border = True):
        col4, col5, col6,col7 = st.columns(4)
        with col4:
            st.image('./picture.jpg')
            st.write("actor1")
        with col5:
            st.image('./picture.jpg')
            st.write("actor2")
        with col6:
            st.image('./picture.jpg')
            st.write("actor3")
        with col7:
            st.image('./picture.jpg')
            st.write("actor4")
    
with col3:
    st.markdown(
    """
    <style>
    .title {
        font-size: 24px;  /* Adjust the font size */
        font-weight: bold; /* Adjust the font weight */
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
    st.markdown("<h6 style='color: black;'>Similar Movies</h1>", unsafe_allow_html=True)
    with st.container(border = True):
        st.image('./picture.jpg')
        st.write("movie1")
        st.image('./picture.jpg')
        st.write("Movie2")
        st.image('./picture.jpg')
        st.write("Movie3")
        

    
    

    

        

