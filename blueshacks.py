import streamlit as st
import webbrowser
 
st.write("""
Breaking Barriers - Blues Project Idea
""")

url = 'https://dmoj.ca'

school = st.button('Learn to Interact in a classroom setting')
if school:
 webbrowser.open_new_tab(url)
