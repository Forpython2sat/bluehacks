import streamlit as st

col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25, 0.25])

with col1:
  with st.container():
    st.header('Lesson 1: Basics')
    image1 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(10).png"
    st.image(image1)
    st.link_button("Review your skills ", "https://blueshackst.streamlit.app/")
  st.header('Lesson 5: Group Projects')
  image5 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(11).png"
  st.image(image5)
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")
  
with col2:
  with st.container():
    st.header('Lesson 2: Asking Questions')
    image2 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(12).png"
    st.image(image2)
    st.link_button("Learn to Interact Smoothly with Peers", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 6: Asking for Extensions')
  image6 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(13).png"
  st.image(image6)
  st.link_button("Learn to Talk with Strangers", "https://bluehacks-4.streamlit.app")
 
with col3:
  with st.container():
    st.header("Lesson 3: Email Etiquette")
    image3 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(15).png"
    st.image(image3)
    st.link_button("How to compose an effective email", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 7: In-Class Conversation')
  image7 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(14).png"
  st.image(image7)
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")

with col4:
  with st.container():
    st.header("Lesson 4: Extra Help")
    image4 = ("https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(8).png")
    st.image(image4)
    st.link_button("How to compose an effective email", "https://blueshacks2.streamlit.app/")
    
  st.header('Lesson 8: Presentations')
  image8 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(16).png"
  st.image(image8)
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")

