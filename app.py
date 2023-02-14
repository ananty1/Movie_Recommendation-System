import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import requests

with st.sidebar:
    selectedmenu=option_menu(
        menu_title="Main Menu",
        options=["Home","Projects","Contacts"],
        default_index=0,
        orientation="horizontal",
    )
if selectedmenu=='Home':
    def fetchposter(movie_id):
        url=f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=73ea8b3ecf4e69a185157298d93f8b48'
        # print(type(movie_id),"the index of the current",url)
        response=requests.get(url)
        data=response.json()
        return "https://image.tmdb.org/t/p/w500"+data['poster_path']



    similaity=pickle.load(open('similaity.pkl','rb'))

    def recommend(movie):
        movie_index=newdf[newdf['title']==movie].index[0]
        similar=similaity[movie_index]
        movies_list=sorted(list(enumerate(similar)),reverse=True,key=lambda x:x[1])[1:6]
        # movie_id=sorted(list(enumerate(similar)),reverse=True,key=lambda x:x[0])[1:6]
        # print(movies_list)
        recommend_movies=[]
        recommend_posters=[]
        for el in movies_list:
            recommend_movies.append(newdf.iloc[el[0]].title)
            recommend_posters.append(fetchposter(newdf.iloc[el[0]].movie_id))
        return (recommend_movies,recommend_posters)


    newdf=pickle.load(open('movies.pkl','rb'))
    st.title('Movie Recommendar System')

   

    movie_selected=st.selectbox('Movies list',newdf['title'].values)
    movie_index=newdf[newdf['title']==movie_selected].index[0]
    if st.button('Recommend'):
        recommend_movies,recommend_posters=recommend(movie_selected)#

        col2, col3  = st.columns(2)
        with col2:
            st.write(recommend_movies[0])
            st.image(recommend_posters[0])
            # st.write(recommend_posters[0])

        with col3:
            st.write(recommend_movies[1])
            st.image(recommend_posters[1])

        
        
        col4, col5 ,col6  = st.columns(3)
        with col4:
                st.write(recommend_movies[2])
                st.image(recommend_posters[2])
        
        with col5:
                st.write(recommend_movies[3])
                st.image(recommend_posters[3])

        with col6:
                st.write(recommend_movies[4])
                st.image(recommend_posters[4])

if selectedmenu=='Projects':
    st.title("This is project menu")

if selectedmenu=="Contacts":
    st.title("This is contact page.")
