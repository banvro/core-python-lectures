import streamlit as st

st.header("More Input fields")

st.selectbox("Chhose your gender", ["Male", "Female", "other"])

st.multiselect("Choose your interset", 
               ["C++", "java", "Python", "javaScript", "Pascal", "Colobo", "Swift", "React"],
               default = "Python",
               help = "Choose multiple as your need",
               placeholder = "Choose your intrest",
               max_selections = 3,
                # label_visibility = "collapsed"
               )

st.radio("Choose your gender", ["Male", "Female", "Other"], horizontal = True)

x = st.checkbox("Cources")

# st.write(x)

y = st.toggle("Theam", label_visibility = "visible")

# st.write(y)
if y:
    st.success("You are active..1")
    
st.slider("Choose your age",
          max_value = 70, min_value = 20, step = 5)

st.select_slider("Choose", ["Apple", "Banna", "Orange"])

st.color_picker("Choose your fvrt color", value = "#AFFF0F")

st.file_uploader("Choose your resume")

# st.ca 

st.button("Submit", type = "primary")

st.download_button("Download File", "hello how are you!", "x.txt")

st.link_button("Go to Programography", "https://programography.com")

st.feedback(options = "thumbs")

st.feedback(options = "faces")

st.feedback(options = "stars")


st.chat_input("Enter your query..")
