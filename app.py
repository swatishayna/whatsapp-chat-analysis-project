import pandas as pd
import numpy as np
import emoji
import plotly.express as px
from collections import Counter
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from src.utils import readloadchat


data = [] # List to keep track of data so it can be used by a Pandas dataframe
conversation = readloadchat.get_whatsapp_txt_file()

with open(conversation, encoding="utf-8") as fp:
    fp.readline() # Skipping first line of the file because contains information related to something about end-to-end encryption
    messageBuffer = [] 
    parsedData = []
    date, time, author = None, None, None
    while True:
        line = fp.readline() 
        
        if not line: 
            break
        line = line.strip() 
        print("***************",line)
        if readloadchat.startsWithDateAndTime(line): 
            
            if len(messageBuffer) > 0: 
                parsedData.append([date, time, author, ' '.join(messageBuffer)]) 
            messageBuffer.clear() 
            date, time, author, message = readloadchat.getDataPoint(line) 
            messageBuffer.append(message) 
        else:
            messageBuffer.append(line)


df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Author', 'Message']) # Initialising a pandas Dataframe.
df = readloadchat.clean_date_col(df)
df["Date"] = pd.to_datetime(df["Date"])








readloadchat.delete_whatsapptxtfile()
