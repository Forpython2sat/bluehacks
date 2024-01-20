import streamlit as st

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

ai = st.chat_message('ai')
user = st.chat_message('user')

ai.write("Hello 👋")
ai.write("Let us learn how to communicate effectively with peers and friends!")
ai.write("Click any button to get started")

if st.button('Learn to strike up a conversation', on_click=click_button):
    ai.write('''Often, our conversations are cut short after a simple "hello," and we are launched into a state of awkwardness.''')
    ai.write("According to psychology, however, people typically tend to engage more when the conversation is something that concerns them or interests them.")
    ai.write("Therefore, if you know that something has been on their minds, talk to them about it.")
if st.button('Learn to elegantly decline', on_click=click_button):
    ai.write("Often our friends can unkowningly ask us something that we are uncomfortable with.")
    ai.write("Therefore, it is essential to know how to decline.")
    ai.write("Usually, it is best to be up front about it, and hold your ground despite the pressure.")
