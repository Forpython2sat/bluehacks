import streamlit as st

#This will be the page that will be redirected when the interact with a peer/friend button is clicked
with st.chat_message("user"):
    st.write("Hello 👋")
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
