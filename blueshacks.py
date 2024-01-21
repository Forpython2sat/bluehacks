import streamlit as st

col1, col2, col3 = st.columns(3)
container_width = st.get_container_width
screen_width = st.screen_width
st.write(screen_width)

with col1:
  st.header('Interacting With Teachers')
  st.link_button("Learn to be heard in the classroom", "https://blueshackst.streamlit.app/")

with col2:
  st.header('Interacting with peers')
  st.link_button("Learn to ", "https://blueshacks2.streamlit.app/")
with col3:
  st.header('Questionaires and Quizes to Test Your Knowledge')
  st.link_button("Lesson 1 Quiz", "https://1e12b53b-1124-4840-b699-e696e74c47be-00-1tulldaqgf3jp.janeway.replit.dev/")
  st.link_button("Lesson 2 Quiz", "https://4248fbdf-37ea-423a-964b-16e6fba16303-00-x94itf3kt79e.spock.replit.dev/")
  st.link_button("Lesson 3 Quiz", "https://b407031c-3d95-4e7b-b8db-3eae7d1f240d-00-2tq3v4cwm7zqd.janeway.replit.dev/")
  st.link_button("Lesson 4 Quiz", "https://0f0c1507-87bb-4da5-aedc-4a5e9f795bf1-00-2yb8dchn9mbx1.kirk.replit.dev/")
