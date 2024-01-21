import streamlit as st

outl = ['Lesson 1: Interacting with a Teacher', "1. Address them with their appropriate title (i.e. Mr., Ms., Dr., Professor, etc).", "2. Be polite and use formal language, especially in educational settings.", "3. Ask questions when you need clarification on a topic.", "4. Listen actively and engage in discussions related to the subject." ]

def counterplus():
    st.session_state.counter += 1

if "messages" not in st.session_state:
    st.session_state.messages = []

if 'counter' not in st.session_state:
    st.session_state.counter = -1

with st.chat_message('ai'):
    st.write('"Hello 👋"')
    st.write("Today, we will learn how to communicate effectively with a teacher.")
    st.write("Remember to: ")
    
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input(placeholder='Say something', on_submit=counterplus)
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    if st.session_state.counter >= len(outl):
        response = 'That is it for this lesson. I hope you learned something!'
    else:
        response = outl[st.session_state.counter]
    with st.chat_message('ai'):
        st.markdown(response)
    st.session_state.messages.append({'role': 'ai', 'content': response})
