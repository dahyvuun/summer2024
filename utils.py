from langchain_core.callback.base import BaseCallbackHandler

class StreamHandler(BasecCallbackHandler):
    def __init__(self,container, initial_text=""):
        self.container=container
        self.text=initial_text
        
    def on_llm_new_token(self, token:str, **kwargs) ->None:
        self.text += token
        self.container.markdown(self.text)


import streamlit as st

def print_messages():

    if "messages" in st.session_state and len(st.session_state["messages"])>0:
        for chat_message in st.session_state["messages"]:
            st.chat_message(chat_message.role).write(chat_message.content)
            