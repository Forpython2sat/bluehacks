import streamlit as st
import webbrowser
 
st.write("""
Breaking Barriers - Blues Project Idea
""")

url = "https://dmoj.ca/user/laight"
if st.button('Learn to Interact in a classroom setting'):
 webbrowser.open_new_tab(url)
