import streamlit as st


st.set_page_config(
    page_title="FAQ",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebare.selectbox('Choisissez votre modèle', ["Modèle 1", "Modèle 2", "Modèle 3"])

st.title("FAQ")

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("Comment puis-je vous aider ?"):

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Appel de l'API
    response = f"Echo: {prompt}"
    
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
