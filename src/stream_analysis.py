import streamlit as st
from src.utils import readloadchat, analysis

def app():
    try:
        df = readloadchat.readdf()
        
        choice = st.sidebar.selectbox('Select: ', ( 'Detailed analysis','emoji analysis', 'word cloud'))
        if choice == 'Detailed analysis':
            Unique_User = st.checkbox("Unique User")
            if Unique_User:
                st.write(analysis.get_unique_user(df))
            chat_stat = st.checkbox("Group Chat Stats")
            if chat_stat:
                st.write(analysis.chatstat(df)[0])
            user_analysis = st.checkbox(" User wise chat stat")
            if user_analysis:
                option = st.selectbox('Select', ('All user analysis', 'Individual User analysis'))
                if option == 'All user analysis':
                    st.dataframe(analysis.user_wise_analysis(df))
                elif option == 'Individual User analysis':
                    user = st.selectbox('Select the user', (analysis.get_unique_user(df)))
                    st.dataframe(analysis.user_wise_analysis(df,user))




        if choice == 'emoji analysis':
            st.sidebar.radio("",["Group Chat emoji Analysis", "Individual User emoji Analysis"])
        if choice == 'word cloud':
            st.sidebar.radio("",["Group Chat World Cloud", "Individual User World Cloud"])
    except:
        st.write("Upload Your Group Chat File")




    