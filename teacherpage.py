import streamlit as st

outl = ["1. Address them with their appropriate title (i.e. Mr., Ms., Dr., Professor, etc). Understood?", "2. Be polite and use formal language, especially in educational settings. Got that?", "3. Ask questions when you need clarification on a topic. Don't be afraid!", "4. Listen actively and engage in discussions related to the subject. And that is it!", "Good luck communicating!" ]

def counterplus():
    st.session_state.counter += 1

if "messages" not in st.session_state:
    st.session_state.messages = []

if 'counter' not in st.session_state:
    st.session_state.counter = -1

if 'checker' not in st.session_state:
    st.session_state.checker = False

with st.chat_message('ai'):
    st.write('Hello! 👋')
    st.write("Today, we will learn the basics of communicating with a teacher.")
    st.write("Are you ready to start?")
    
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input(placeholder='Say something', on_submit=counterplus)
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    if st.session_state.counter >= len(outl):
        response = ('''That is it for this lesson. I hope you learned something!
                    Below is a quiz going through the information you've learned today. Give it a try!''')    
        st.session_state.checker = True
    else:
        response = outl[st.session_state.counter]
    with st.chat_message('ai'):
        st.markdown(response)
        if st.session_state.checker:
            st.link_button("Lesson 1 Quiz", "https://1e12b53b-1124-4840-b699-e696e74c47be-00-1tulldaqgf3jp.janeway.replit.dev/")
    st.session_state.messages.append({'role': 'ai', 'content': response})
