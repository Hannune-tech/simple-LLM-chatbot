import streamlit as st
from dotenv import load_dotenv
import config as cfg
from copy import deepcopy
from send_requests import send_request

send_request = send_request()
load_dotenv()

def main():
    
    with st.sidebar:
        # Select api provider and models list
        st.write("***")
        api_provider = st.selectbox("Select API provider", ["OpenAI", "Ollama"])        
        models_list = send_request.get_models_list(api_provider)
        model = st.selectbox("Select model", models_list)

        st.write(f"API provider: {api_provider}")
        st.write(f"Model: {model}")

        st.session_state["api_provider"] = api_provider
        st.session_state["model"] = model


        st.write("***")
        if st.button("Reset"):
            reset()
        if st.button("Reset messages"):
            set_messages()
    
    # Initialize messages
    if "messages" not in st.session_state:
        set_messages() 

    # Chat interface
    chat()
    

    
def chat():
    for message in st.session_state.messages:
        if message["role"] == "system":
            continue
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Temporarily update the last message with the augmented input
        _messages = deepcopy(st.session_state.messages)
        _messages[-1]["content"] = prompt

        # Generate response with augmented input
        response = send_request.post_chat(
            st.session_state["api_provider"],
            _messages,
            st.session_state["model"]            
            )

        with st.chat_message("assistant"):
            st.markdown(response)

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})


def reset():
    for key in st.session_state:
        del st.session_state[key]


def set_messages():
    st.session_state["messages"] = []
    st.session_state["messages"].append({"role": "system", "content": cfg.system_message})



if __name__ == "__main__":
    main()