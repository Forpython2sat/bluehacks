import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
import json

st.write(f"Screen width is {streamlit_js_eval(js_expressions='window.innerWidth', key = 'SCR')}")
st.write(f"Screen height is {streamlit_js_eval(js_expressions='window.innnerHeight', key = 'SCR1')}")

st.write("""
joe biden
""")

htp="https://raw.githubusercontent.com/Forpython2sat/bluehacks/main/art/teacher.png"
st.image(htp, caption= "joe biden", width=350)

st.link_button("dmoj link", "https://dmoj.ca/user/laight")
st.link_button("Learn to Interact in a Classroom Environment", "https://blueshackst.streamlit.app/")
st.link_button("Learn to Interact Smoothly with Peers", "https://blueshacks2.streamlit.app/")

