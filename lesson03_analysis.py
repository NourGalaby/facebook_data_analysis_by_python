import pickle
import pandas as pd 
import string
from operator import itemgetter
loaded_data= pickle.load(file=open("steam_data.pkl"))

df2 = pd.io.json.json_normalize(data=loaded_data)

months=["january",
"february",
"march",
"april",
"May",
"june",
"july",
"august",
"september",
"october",
"november",
"december"]

def count_words(df):
    stop_words=["a","about","above","after","again","against","all","am","an","and","any","are","now",
"aren't","as","at","be","because","been","before","being","below","between","both","but","by",
"can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down",
"during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having",
"he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's",
"i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more",
"most","mustn't","my","myself","no","nor","not","of",
"off","on","once","only","or","other","ought","our",
"ours	ourselves","out","over","own","same","shan't",
"she","she'd","she'll","she's","should","shouldn't","so",
"some","such","than","that","that's","the","their","theirs",
"them","themselves","then","there","there's","these","they",
"they'd","they'll","they're","they've","this","those","through",
"to","too","under","until","up","very","was","wasn't","we","we'd",
"we'll","we're","we've","were","weren't","what","what's","when","when's",
"where","where's","which","while","who","who's","whom","why","why's","with",
"won't","would","wouldn't","you","you'd","you'll","you're","you've","your",'guys','just','day',
"yours","yourself","yourselves","will","ana","isa","can","hwa","wala","msh","wla","hya","will",'enta','7aga','mesh','dah','bas','elly','b2a','3ala','alf','enty','3al',]


  #  steam_stop_words=["steam","follow","avaiable","game","well",'page',"time","save","facebook","twitter","wherever","notification","instant"]
    words={}
    mapping = dict.fromkeys(map(ord, string.punctuation))
    for m in df2['message']:
        try:
            sent=m.split(' ')
        except:
            pass
           # print "ERROR"+str(m) 
        for word in sent:
                word=word.strip()
                word=word.translate( mapping) #remove punctation
                word=word.lower()
                if len(word)<3: #skip if 2 chars or less
                    continue
                if word in stop_words : #skip if common 
                    continue
                if word in words:
                    words[word]+=1
                else:
                    words[word]=1
    print("done counting words")
    return words       


# Words
words = count_words(df2)

#replace Nan
df2.fillna("",inplace=True)

#make new column
words_df=pd.DataFrame(words.items(), columns=['Word', 'count'])

#sort 
sorted_words=sorted(words.items(), key=itemgetter(1),reverse=True)

#
words_df[ words_df['count'] > 1000 ].plot(x='Word',kind='bar')


#
metal_posts=df2[df2.message.str.contains("metal")]
df2['csgo']=df2.message.str.contains("CS.?GO|Counter Strike")
df2['lol']=df2.message.str.contains("League Of Legends|LOL")
df2['free']=df2.message.str.contains("free")
df2['daily']=df2.message.str.contains("daily")

df2.groupby(by=df2.csgo).count()
words_df[ words_df['count'] > 10 ]
print words_df[ words_df['Word'].isin(months) ]
