import streamlit as st

col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")

with col1:
  st.header('Interact in a Classroom Environment')
  st.link_button("Learn to Interact in a Classroom Environment", "https://blueshackst.streamlit.app/")
with col1:
  st.header('Interact Smoother with Your Peers')
  st.link_button("Learn to Interact Smoothly with Peers", "https://blueshacks2.streamlit.app/")

