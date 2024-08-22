from packages.AI import Model
import streamlit as st 
from utils import print_messages
from langchain_core.messages import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["OPEN_API_KEY"] = st.secrets["OPENAI_API_KEY"]
def main():
    model = Model()

    st.title("2024 HAI Summer Project")
    st.markdown("---")

    st.subheader("Google Gemini Api를 이용해 대화 주고받기")
    query = st.text_input('INPUT', "Gemini에게 보낼 메시지 입력")
    response = model(query)

    st.markdown("---")
    st.markdown("### **OUTPUT**")
    st.markdown(response)

    if "messages" not in st.session_state:
        st.session_state["messages"]=[]
    print_messages()
        
    if "messages" in st.session_state and len(st.session_state["messages"])>0:
        for role, message in st.session_state["messages"]:
            st.chat_message(role).write(message)


    if query := st.chat_input("메세지를 입력해주세요."):
        st.chat_message("user").write(f"{query}")
        st.session_state["message"].append(ChatMessage(role="user", content=query))

        prompt = ChatPromptTemplate.from_template(
            """질문에 대해 간결히 답변해 주세요. {question}"""
        )

        chain = prompt | ChatOpenAI() | StrOutputParser()
        response=chain.invoke({"question":user_input})
        msg=response.content

        with st.chat_message("assistant"):
            msg = f"당신이 입력한 내용: {query}"
            st.write(msg)
            st.session_state["messages"].append(("assistant", msg))

if __name__ == "__main__":
    main()
