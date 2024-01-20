import streamlit as st

#This will be the page that will be redirected when the interact with a peer/friend button is clicked
animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

with st.chat_message("user"):
    st.write("Hello 👋")
    st.write("Let us learn how to communicate effectively with peers and friends!")

inp = st.chat_input('Type to continue: ')

if inp:
    if st.button('Learn to strike up a conversation'):
        with st.chat_message("user"):
            st.write('''Often, our conversations are cut short after a simple "hello," and we are launched into a state of awkwardness.''')
            st.write("According to psychology, however, people typically tend to engage more when the conversation is something that concerns them or interests them.")
            st.write("Therefore, if you know that something has been on their minds, talk to them about it.")
