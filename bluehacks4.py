import streamlit as st

outl = ['1. Start with a polite greeting.', '2. Be open and approachable. Keep in mind that strangers may not share the same interests that you do.', '3. Listen actively.', '4. Respect the personal boundaries of others.']

def counterplus():
    st.session_state.counter += 1

if "messages" not in st.session_state:
    st.session_state.messages = []

if 'counter' not in st.session_state:
    st.session_state.counter = -1

if 'checker' not in st.session_state:
    st.session_state.checker = False

with st.chat_message('ai'):
    st.write('Hello 👋')
    st.write('''We will now start Lesson 4: Interacting with Strangers.
    Interacting with strangers can be a daunting, yet common and neccesary occurance in a wide variety of situations. Here are some times for effective communication.''')
    
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
            st.link_button("Lesson 4 Quiz", "https://0f0c1507-87bb-4da5-aedc-4a5e9f795bf1-00-2yb8dchn9mbx1.kirk.replit.dev")
    st.session_state.messages.append({'role': 'ai', 'content': response})
