import streamlit as st
from src.utils import readloadchat
import pandas as pd




def app():
    try:
        df = readloadchat.readdf()
        st.dataframe(df)
    except:
        st.write("Upload Your Group Chat File")

