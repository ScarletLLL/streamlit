import streamlit as st
import pandas as pd

st.title("Major US Stocks AI Forecast Wizard")

df=pd.read_csv('df_model.csv')
st.table(df)