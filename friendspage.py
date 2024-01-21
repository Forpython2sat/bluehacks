import streamlit as st

outl = ['We will first learn how to open conversations. Opening conversations are sometimes quite challenging, and often times, the conversation halts after an exchange of greetings. What would you do to prevent this from happening?', 'Usually, we should talk about something that they are interested in. Psychology shows that humans tend to engage more when something is about them, or if something interests them. Thus, next time you see your friend, ask him whats going good for them, what may be troubling him, and also ask them about their hobbies.']

def counterplus():

def counterplus():
    st.session_state.counter += 1

if "messages" not in st.session_state:
    st.session_state.messages = []

if 'counter' not in st.session_state:
    st.session_state.counter = -1

if 'checker' not in st.session_state:
    st.session_state.checker = False

with st.chat_message('ai'):
    st.write('"Hello 👋"')
    st.write("Today, we will learn how to effectively communicate with our peers.")
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
            st.link_button("Lesson 2 Quiz", "https://4248fbdf-37ea-423a-964b-16e6fba16303-00-x94itf3kt79e.spock.replit.dev")
    st.session_state.messages.append({'role': 'ai', 'content': response})
