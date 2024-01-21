import streamlit as st

col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25, 0.25])

with col1:
  with st.container():
    st.header('Lesson 1: Basics')
    st.link_button("Learn to Interact in a Classroom Environment", "https://blueshackst.streamlit.app/")
  st.header('Lesson 3: Professionals')
  image3 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/teacher2.png"
  st.image(image3)
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")
    
  
with col2:
  with st.container():
    st.header('Lesson 2: Asking Questions')
    st.link_button("Learn to Interact Smoothly with Peers", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 4: Strangers')
  image4 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(2).png"
  st.image(image4)
  st.link_button("Learn to Talk with Strangers", "https://bluehacks-4.streamlit.app")

with col3:
  with st.container():
    st.header("Lesson 3: Email Etiquette")
    st.link_button("How to compose an effective email", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 3: Professionals')
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")

with col4:
  with st.container():
    st.header("Lesson 4: osama")
    st.link_button("How to compose an effective email", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 3: Professionals')
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")
