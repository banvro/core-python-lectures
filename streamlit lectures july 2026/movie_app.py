import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide")

st.title("Movie App")

data = pd.read_csv("imdb_top_1000.csv").head(50)

# st.dataframe(data)

for i in range(0, len(data), 4):
    
    col1, col2, col3, col4 = st.columns(4)
    
    for col, (_, movie) in zip([col1, col2, col3, col4], data.iloc[i : i+4].iterrows()):
        
        with col:
            with st.container(border = True):
                with st.container(border = True, horizontal_alignment = "center"):
                    st.image(movie["Poster_Link"], width = 250)
                st.text(movie["Series_Title"][ : 20])
                
                st.warning(movie["Genre"])
                
                st.text(f"⭐ {movie["IMDB_Rating"]} / 10  ({movie["No_of_Votes"]})         💲 {movie["Gross"]}")
                
                with st.popover("More about movie"):
                    st.text(movie["Overview"])
                    
                    st.success(f"{movie["Star1"]},  {movie["Star2"]}, {movie["Star3"]},  {movie["Star4"]}")
