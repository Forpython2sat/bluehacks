import streamlit as st

col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25, 0.25])

with col1:
  with st.container():
    st.header('Lesson 1: Basics')
    image1 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(10).png"
    st.image(image1)
    st.link_button("Review your skills ", "https://blueshackst.streamlit.app/")
  st.header('Lesson 5: Projects')
  image5 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(11).png"
  st.image(image5)
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")
  
with col2:
  with st.container():
    st.header('Lesson 2: Questions')
    image2 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(12).png"
    st.image(image2)
    st.link_button("Get help in class", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 6: Extensions')
  image6 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(13).png"
  st.image(image6)
  st.link_button("Manage your deadlines", "https://bluehacks-4.streamlit.app")
 
with col3:
  with st.container():
    st.header("Lesson 3: Emails")
    image3 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(15).png"
    st.image(image3)
    st.link_button("Compose effective emails", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 7: Participating')
  image7 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(14).png"
  st.image(image7)
  st.link_button("Participate in class", "https://bluehacks-3.streamlit.app")

with col4:
  with st.container():
    st.header("Lesson 4: Extra Help")
    image4 = ("https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(8).png")
    st.image(image4)
    st.link_button("Arrange for afterschool help", "https://blueshacks2.streamlit.app/")
    
  st.header('Lesson 8: Presentations')
  image8 = "https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/Untitled%20(16).png"
  st.image(image8)
  st.link_button("Present more effectively", "https://bluehacks-3.streamlit.app")

