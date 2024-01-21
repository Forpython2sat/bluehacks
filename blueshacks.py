import streamlit as st

col1, col2 = st.columns([0.5, 0.5])

with col1:
  with st.container():
    st.header('Lesson 1: Teachers')
    image1 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/teacher.png"
    st.image(image1)
    st.link_button("Learn to Interact in a Classroom Environment", "https://bluehacks-menu.streamlit.app")
  st.header('Lesson 3: Professionals')
  image3 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/teacher2.png"
  st.image(image3)
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")
    
  
with col2:
  with st.container():
    st.header('Lesson 2: Peers')
    image2 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Humaaans%20Friend%20Meeting.png"
    st.image(image2)
    st.link_button("Learn to Interact Smoothly with Peers", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 4: Strangers')
  image4 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(2).png"
  st.image(image4)
  st.link_button("Learn to Talk with Strangers", "https://bluehacks-4.streamlit.app")
