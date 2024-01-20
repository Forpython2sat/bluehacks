import streamlit as st

#This will be the page that will be redirected when the interact with a peer/friend button is clicked
prompt = st.chat_input("Say something")
with st.chat_message("user"):
    st.write("Hello 👋")
with st.chat_message("user"):
    st.write("Let us learn how to communicate effectively with peers and friends!")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
