import streamlit as st
from src.utils import readloadchat


def app():
    st.write("working fine")
    docx_file = st.file_uploader("Upload File",type=['txt'])
    if st.button("Process"):
        if docx_file is not None:
            file_details = {"Filename":docx_file.name,"FileType":docx_file.type,"FileSize":docx_file.size}
            
            if docx_file.type == "text/plain":
                
                mesage = readloadchat.save_uploaded_file(docx_file)
                readloadchat.read_uploaded_save_csv()
                st.write(mesage)

                