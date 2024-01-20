import streamlit as st

ai = st.chat_message('ai')
user = st.chat_message('user')

ai.write("Hello 👋")
ai.write("Let us learn how to communicate effectively with peers and friends!")

if st.button('Learn to strike up a conversation'):
    ai.write('''Often, our conversations are cut short after a simple "hello," and we are launched into a state of awkwardness.''')
    ai.write("According to psychology, however, people typically tend to engage more when the conversation is something that concerns them or interests them.")
    ai.write("Therefore, if you know that something has been on their minds, talk to them about it.")

inp = st.chat_input('Say something: ')

if inp:
    user.write(inp)
