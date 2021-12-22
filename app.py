import streamlit as st

# Custom imports
from src.multipage import MultiPage
from src import stream_analysis,stream_chatdf,stream_upload_data

try:
    # Create an instance of the app

    apps = MultiPage()

    # Add all your applications (pages) here
    apps.add_page("Upload Chat File", stream_upload_data.app)
    apps.add_page("View Chat",    stream_chatdf.app)
    apps.add_page("Analysis", stream_analysis.app)
    
except:
    pass






if __name__ == "__main__":
    apps.run()