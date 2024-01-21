import streamlit as st

col1, col2 = st.columns(2)
col1.write("this is column 1")
col2.write("this is column 2")

col1.write("""
joe biden
""")

htp="https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/teacher.png"
col1.image(htp, caption= "joe biden", width=100)

col1.link_button("dmoj link", "https://dmoj.ca/user/laight")
col2.link_button("Learn to Interact in a Classroom Environment", "https://blueshackst.streamlit.app/")
col2.link_button("Learn to Interact Smoothly with Peers", "https://blueshacks2.streamlit.app/")

