# Importing libraries
import streamlit as st
import os 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from langchain_experimental.agents import create_pandas_dataframe_agent 
from langchain_openai import OpenAI

st.title("FinGPT Application")

#setup the api key 
OPENAI_API_KEY="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"
os.environ['OPENAI_API_KEY']=OPENAI_API_KEY

# Importing the data
df = pd.read_csv('df_model.csv') 
# Initializing the agent 
# We have kept verbose= True. It will print all the intermediate steps during the execution.
model_name="gpt-3.5-turbo-instruct"
agent = create_pandas_dataframe_agent(OpenAI(temperature=0,model=model_name), df, verbose=True) 
 # temperature parameter is used to adjust the creativity of the model.When it is set to 0, the model is least prone to hallucination.
openai = OpenAI(temperature=0.0,model=model_name)  
openai.model_name # This will print the model being used, 
                  # by default it uses ‘text-davinci-003’

st.table(df_model)