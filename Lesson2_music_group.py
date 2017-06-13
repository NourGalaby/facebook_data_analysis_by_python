import requests 
import time
import pickle
import random

token = "EAACEdEose0cBAHNK1EOFPJeFXkTSXsZA27FlYBVfRt3ARNyXK757TjgCvHq0TeftavCDHQuQhtVFbmLr9ZBDpeyi837Oe2rC6BJKdxdFHKmfelstZC9MhZAKfclRcfqtUwRwRyXYyACYFRnkwltRzC4vlcbwGmB5a9kLhrBu484gatLtCuWWf3dRbuXgKCoZD"

#req="Steam?fields=posts.limit(50){message}"

def req_facebook(req):
    r = requests.get("https://graph.facebook.com/v2.8/" + req , {'access_token' : token})

    return r
    

req="7729761102?fields=feed.limit(20){message,comments,created_time}"
results=req_facebook(req).json()


data=[]
results=results['feed']
#results=requests.get(results['paging']['next']).json()
i=0
while True:

    try:
        time.sleep(random.randint(3,6))
        data.extend(results['data'])
        r=requests.get(results['paging']['next'])
        results= r.json()    
        i += 1
   
#        if i > 5:
#            break
    except:
        print "done"
        break 
    
    

    
pickle.dump(data,open("buyandsell_group.pkl","wb"))

loaded_data= pickle.load(file=open("buyandsell_group.pkl"))