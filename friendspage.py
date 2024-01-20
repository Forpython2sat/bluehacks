import streamlit as st

def userout(s):
    with st.chat_message("user"):
        st.write(s)

def aiout(s):
    with st.chat_message('ai'):
        st.write(s)

aiout("Hello 👋")
aiout("Let us learn how to communicate effectively with peers and friends!")

inp = st.chat_input('Say something: ')

if inp:
    userout(inp)
    if st.button('Learn to strike up a conversation'):
        aiout('''Often, our conversations are cut short after a simple "hello," and we are launched into a state of awkwardness.''')
        aiout("According to psychology, however, people typically tend to engage more when the conversation is something that concerns them or interests them.")
        aiout("Therefore, if you know that something has been on their minds, talk to them about it.")
