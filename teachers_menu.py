import streamlit as st

col1, col2, col3, col4 = st.columns([0.25, 0.25, 0.25, 0.25])

with col1:
  with st.container():
    st.header('Lesson 1: Basics')
    st.link_button("Review your skills ", "https://blueshackst.streamlit.app/")
  st.header('Lesson 5: Group Projects')
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")
    
  
with col2:
  with st.container():
    st.header('Lesson 2: Asking Questions')
    st.link_button("Learn to Interact Smoothly with Peers", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 6: Asking for Extensions')
  st.link_button("Learn to Talk with Strangers", "https://bluehacks-4.streamlit.app")

with col3:
  with st.container():
    st.header("Lesson 3: Email Etiquette")
    st.link_button("How to compose an effective email", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 7: In-Class Conversation')
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")

with col4:
  with st.container():
    st.header("Lesson 4: Extra Help")
    st.link_button("How to compose an effective email", "https://blueshacks2.streamlit.app/")
  st.header('Lesson 8: Presentations')
  st.link_button("Learn to Communicate with Professionals", "https://bluehacks-3.streamlit.app")
