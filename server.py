import streamlit as st
import openai
from streamlit_lottie import st_lottie
from io import StringIO
from process import ProcessText
from kw import Kw
from app import App
from lang_model import LLM

st.set_page_config(
            page_title='PaperPunch'
        )

application = App()

head_col1, head_col2 = st.columns(2)
lotti_1 = application.load_lotti("https://lottie.host/c3a934fd-27cb-4614-867b-b861840a6919/TuJdvudB1s.json")
with head_col1:
    st.write('Hey buddy,')
    st.title("What's All This Text About?")
with head_col2:
    st_lottie(lotti_1, height=250, width=450)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API key", value="", type="password")
    if st.button('Save'):
        st.success("API Key saved successfully!")

    st.caption(
            "*If you don't have an OpenAI API key, get it [here](https://platform.openai.com/account/api-keys).*")
    openai.api_key = openai_api_key

st.subheader('Because who needs the boring parts? 😈')

ptext = ProcessText()
LLM = LLM()

cola, colb = st.columns(2)
with cola:
    summary_type = st.selectbox('Summary Type', ['Bullet points', '1 Sentence', '5 Sentences', 'Short'])
with colb:
    num_of_kw = st.selectbox('Total Key-words', range(2, 20))
text = st.file_uploader('Choose your file')
alt_text = st.text_area('Or paste your text here:')

process = st.button('Process')
if st.session_state.get('button') != True:
    st.session_state['button'] = process

if st.session_state['button']:
    if text is not None:
        stringio = StringIO(text.getvalue().decode("utf-8")).getvalue()

    else:
        if alt_text is not None:
            stringio = alt_text

        else:
            st.write('No Text')
            raise ValueError('No Text!')

    # KeyWords
    processed_text = ptext.preprocess(stringio)
    kw = Kw()
    kw.butify(kw.get_kw(processed_text, n=num_of_kw))

    with st.spinner(application.random_spinner_text()):
        # Summary
        try:
            summary = LLM.create_summary(kind=summary_type, text=stringio)
            content = summary.choices[0].message.content
            st.subheader(f'Amigo, Here is a {summary_type} summary for your text:')
            st.write(content)
        except:
            st.warning('Looks Like you have some problems with your API Key, Jump and check it!')


    st.divider()

    # Ask
    if "messages" not in st.session_state:
        st.session_state.messages = []

    chatcol1, chatcol2 = st.columns(2)
    lotti_2 = application.load_lotti("https://lottie.host/c1fdee78-0223-4686-9381-114908518131/RQg76ePE5H.json")
    with chatcol1:
        st.write('')
        st.write('')
        st.subheader('Any more Questions?')
        st.write('Ask me down here ⇣⇣⇣')
    with chatcol2:
        st_lottie(lotti_2, height=180, width=200)

    query = st.chat_input('Ask here')

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask Me anything"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner(application.random_spinner_text()):
            try:
                answer = LLM.answer(text=stringio, query=prompt)
                answer_content = answer.choices[0].message.content
                response = f"{answer_content}"
        # Display assistant response in chat message container
            except:
                st.warning('Looks Like you have some problems with your API Key, Jump and check it!')
                response = ''

        with st.chat_message('The Professor', avatar='professor.png'):
            try:
                st.markdown(response)
            except:
                st.markdown("Not this time buddy, Get a proper key!")

        try:
            st.session_state.messages.append({"role": "assistant", "content": response})
        except:
            pass

