import pandas as pd
import numpy as np
import emoji
import plotly.express as px
from collections import Counter
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from src.utils import analysis


data = [] # List to keep track of data so it can be used by a Pandas dataframe
conversation = 'D:\data science\ineuron\Project\whatsappchatanalysis\data\chat\_chat.txt'

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
        if analysis.startsWithDateAndTime(line): 
            
            if len(messageBuffer) > 0: 
                parsedData.append([date, time, author, ' '.join(messageBuffer)]) 
            messageBuffer.clear() 
            date, time, author, message = analysis.getDataPoint(line) 
            messageBuffer.append(message) 
        else:
            messageBuffer.append(line)


df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Author', 'Message']) # Initialising a pandas Dataframe.
df = analysis.clean_date_col(df)
df["Date"] = pd.to_datetime(df["Date"])
print(df.tail(20))
