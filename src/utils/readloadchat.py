import regex as re
import os
import shutil
import pandas as pd




def get_whatsapp_txt_file():
    directorypath = os.path.join("data","rawdata")
    file = os.listdir(directorypath)
    return os.path.join(directorypath,file[0])


def startsWithDateAndTime(s):
    """
    This will change the format of the data
    """
    pattern = '\[([0-9]+(/[0-9]+)+), ([0-9]+(:[0-9]+)+) (AM|PM|am|pm)]'
    try:
        s = s[:s.index("]")+1]
        result = re.match(pattern, s)
        return True
    except:
         return False
    
   
def FindAuthor(s):
    """ 
    Extract username 
    """
    s=s.split(":")
    if len(s)==2:
        return True
    else:
        return False

        
def getDataPoint(line):   

    splitLine = line.split('] ') 
    dateTime = splitLine[0]
    date, time = dateTime.split(', ') 
    message = ' '.join(splitLine[1:])
    if FindAuthor(message): 
        splitMessage = message.split(': ') 
        author = splitMessage[0] 
        message = ' '.join(splitMessage[1:])
    else:
        author = None
    return date[1:], time, author, message

def clean_date_col(df):
    for count,i in enumerate(df['Date']):
        try:
            i = i.replace("[", "")
        except:
            pass
        finally:
            df["Date"][count] = i 
    return df


def delete_whatsapptxtfile(): 
    if os.path.isdir("data"):
        shutil.rmtree("data")
    os.mkdir("data")
    os.mkdir(os.path.join("data","rawdata"))


def read_uploaded_save_csv():

    data = [] # List to keep track of data so it can be used by a Pandas dataframe
    conversation = get_whatsapp_txt_file()

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
            
            if startsWithDateAndTime(line): 
                
                if len(messageBuffer) > 0: 
                    parsedData.append([date, time, author, ' '.join(messageBuffer)]) 
                messageBuffer.clear() 
                date, time, author, message = getDataPoint(line) 
                messageBuffer.append(message) 
            else:
                messageBuffer.append(line)


    df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Author', 'Message']) # Initialising a pandas Dataframe.
    df = clean_date_col(df)
    df["Date"] = pd.to_datetime(df["Date"])
    df.to_csv(os.path.join("data","chatdf.csv"), index = False)
    



def readdf():
    return pd.read_csv("data\chatdf.csv")

def save_uploaded_file(file):   
    path = os.path.join("data","rawdata")
    try:

        with open(os.path.join(path, file.name), "wb") as f:
            f.write(file.getbuffer())
            return "Uploaded"
    except Exception as e :
        message = "Something went wrong while saving the file in to the data folder"
        return message