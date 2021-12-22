import regex
import emoji
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter
import plotly.express as px
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd





def get_unique_user(df):
    return pd.DataFrame(df.Author.unique(), columns = ['UniqueUsers']).dropna().reset_index(drop=True)

def split_count(text):
        emoji_list = []
        data = regex.findall(r'\X', text)
        for word in data:
            if emoji.is_emoji(word):
                emoji_list.append(word)
                

        return emoji_list

def chatstat(df):
    media_messages = df[df['Message'] == '<Media omitted>'].shape[0]
    

    df["emoji"] = df["Message"].apply(split_count)
    emojis = sum(df['emoji'].str.len())
    
    URLPATTERN = r'(https?://\S+)'
    df['urlcount'] = df.Message.apply(lambda x: regex.findall(URLPATTERN, x)).str.len()
    links = int(np.sum(df.urlcount))
    d = {}
    total_messages = df.shape[0]

    d["Messages:"] = total_messages
    d["Media:"] = media_messages
    d["Emojis:"] = emojis
    d["Links:"] = links
    return d,df


def user_wise_analysis(df,user = None):
    df = chatstat(df)[1]
    media_messages_df = df[df['Message'] == '<Media omitted>']
    messages_df = df.drop(media_messages_df.index)
  
    messages_df['Letter_Count'] = messages_df['Message'].apply(lambda s : len(s))
    messages_df['Word_Count'] = messages_df['Message'].apply(lambda s : len(s.split(' ')))
    messages_df["MessageCount"]=1
    
    l = get_unique_user(df)['UniqueUsers']
    
    d = {}
    user_chatanalysis_df = pd.DataFrame()
    for i in range(len(l)):
    # Filtering out messages of particular user
        req_df= messages_df[messages_df["Author"] == l[i]]
        # username
        d['user'] = l[i]
        # number of messages sent by user, number of rows will tell
        d['Messages_Sent'] =  req_df.shape[0]
        #Word_Count contains of total words in one message. Sum of all words/ Total Messages will yield words per message
        d['words_per_message'] = (np.sum(req_df['Word_Count']))/req_df.shape[0]
        #media conists of media messages
        media = media_messages_df[media_messages_df['Author'] == l[i]].shape[0]
        d['MediaMessagesSent'] = media
        # emojis conists of total emojis
        emojis = sum(req_df['emoji'].str.len())
        d['Emojis Sent'] = emojis
        #links consist of total links
        links = sum(req_df["urlcount"])   
        d['Links Sent'] =  links   
        user_chatanalysis_df = user_chatanalysis_df.append(d, ignore_index=True)
    if user is None:
        return user_chatanalysis_df
    else:
        return user_chatanalysis_df[user_chatanalysis_df['user']==user]



def emoji_analysis(messages_df):
    
    total_emojis_list = list([a for b in messages_df.emoji for a in b])
    emoji_dict = dict(Counter(total_emojis_list))
    emoji_dict = sorted(emoji_dict.items(), key=lambda x: x[1], reverse=True)
    for i in emoji_dict:
        print(i)

def complete_world_cloud(messages_df):
    text = " ".join(review for review in messages_df.Message)
    print ("There are {} words in all the messages.".format(len(text)))
    stopwords = set(STOPWORDS)
    # Generate a word cloud image
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
    # Display the generated image:
    # the matplotlib way:
    plt.figure( figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()



def user_world_cloud(messages_df,user):
    l = ["Aman Kharwal", "Sahil Pansare", "Sumehar"]
    for i in range(len(l)):
        dummy_df = messages_df[messages_df['Author'] == l[i]]
        text = " ".join(review for review in dummy_df.Message)
        stopwords = set(STOPWORDS)
        #Generate a word cloud image
        print('Author name',l[i])
        wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)
        #Display the generated image   
        plt.figure( figsize=(10,5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()