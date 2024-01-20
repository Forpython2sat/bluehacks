import streamlit as st

#This will be the page that will be redirected when the interact with a peer/friend button is clicked

import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'

with st.chat_message("user"):
    st.write("Hello 👋")
with st.chat_message("user"):
    st.write("Let us learn how to communicate effectively with peers and friends!")
    a = st.button("How do I start a conversation?")
    b = st.button("I feel left out of a conversation, how do I join in?")
    c = st.button("I am a little bad at graph theory and my name is Bryant.")
    if a:
        with st.chat_message("user"):
            st.write("Firstly, we should figure out how to initiate a conversation with a friend.")
            st.write('''Often, our conversations are cut short after a simple "hello," and we are launched into a state of awkwardness.''')
            st.write("According to psychology, however, people typically tend to engage more when the conversation is something that concerns them or interests them.")
            st.write("Therefore, if you know that something has been on their minds, talk to them about it.")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
