import streamlit as st

outl = ['1. If needed, address your counterpart with their appropriate title (i.e. Dr., Honourable Minister, etc).', '2. Use formal and respectful language.', "3. Ask questions relevant to your counterpart's expertise.", "4. Prepare questions ahead of your conversation to show you value their time."]
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
    st.write('''We will now start Lesson 3: Interacting with Coworkers and Professionals.
    In some circumstances, it is not appropriate to address coworkers or professionals as peers, for example, when interacting with a doctor, a lawyer, or a senior executive.
    Here, a more formal and respectful approach is required. Following are some tips for effective communication.''')
    
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
            st.link_button("Lesson 3 Quiz", "https://b407031c-3d95-4e7b-b8db-3eae7d1f240d-00-2tq3v4cwm7zqd.janeway.replit.dev")
    st.session_state.messages.append({'role': 'ai', 'content': response})
