import requests 
import time
import pickle
import random
    r = requests.get("https://graph.facebook.com/v2.8/" + req , {'access_token' : token})

    return r
    

req="Steam?fields=posts.limit(50){likes.limit(0).summary(true),comments.limit(0).summary(true),message,created_time}"
results=req_facebook(req).json()


data=[]

results=results['posts']
#results=requests.get(results['paging']['next']).json()
i=0

while True:

    try:
        time.sleep(random.randint(2,4))
        data.extend(results['data'])
        r=requests.get(results['paging']['next'])
        results= r.json()    
        i += 1
   
#        if i > 5:
#            break

    except:
        print "done"
        break 
    
    

    

token = "EAACEdEose0cBAFz07y1Ekbc9TZB3QQUnZB9ZA7QQFv9u0nQxhiKMxoePaSretHjeAXdbJRqHuCj6osI1cu05uaotZBfDNPDkv7jiMZCyzw1NVoQYn7T3IaaJny6adZACAPrkiQ9A7ZBAolgADpfyF2JZAYfliPHxkBobM0gwgrJlwNJpHKMNCQoyZAnEaKFRZA6P8ZD"

#req="Steam?fields=posts.limit(50){message}"

def req_facebook(req):
pickle.dump(data,open("steam_data4.pkl","wb"))

loaded_data= pickle.load(file=open("steam_data4.pkl"))