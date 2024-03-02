from openai import OpenAI
import streamlit as st
from langchain_experimental.agents import create_pandas_dataframe_agent 
from langchain_openai import OpenAI

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

st.title("FinInv Chatbot")
st.caption("A financial chatbot powered by OpenAI LLM")

# Importing the data
df_model = pd.read_csv('df_model.csv') 

# Chatbot
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()



    # Initializing the agent 
    # We have kept verbose= True. It will print all the intermediate steps during the execution.
    model_name="gpt-3.5-turbo-instruct"
    agent = create_pandas_dataframe_agent(OpenAI(temperature=0,model=model_name), df, verbose=True) 
    #client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    #response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    response=agent（st.session_state.messages）
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
