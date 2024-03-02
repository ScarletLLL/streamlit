# Importing libraries
import streamlit as st
import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from langchain_experimental.agents import create_pandas_dataframe_agent 
from langchain_openai import OpenAI


with st.sidebar:
    OPENAI_API_KEY = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#setup the api key 
os.environ['OPENAI_API_KEY']=OPENAI_API_KEY


st.title("FinGPT Assistant")

# Importing the data
df = pd.read_csv('df_model.csv') 

st.table(df_model)




