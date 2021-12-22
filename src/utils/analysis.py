import regex as re





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
    print(splitLine)
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