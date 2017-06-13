#Tutorial 1
#welcome
#graph API
# tokens 
# pandas - anaconda
# simple request


import facebook
import requests
#different versions
2.3 

token = "EAACEdEose0cBAKZBd4ljZBQX51qEWVdqNyYnxZBdN7mk7IPEJFPOagYzPJ2Q3ZBOXlButZBLXmFc4ATnApJ38uXijrxK8YIjGNTxgUmltFfz12I321cQ65HM4mB15MfnwzLiZBfY5JWL3yfDW4FdJH4exFWZBhOZA4bbR5weHkRKkcmxmf2gYzioawGmwZAyZCtqwZD"
#https://developers.facebook.com/tools/explorer/145634995501895/
#graph = facebook.GraphAPI(access_token=TOKEN, version='2.3')





#posts = graph.get_object("7729761102"+req)

def fb_request(req):
    r=requests.get("https://graph.facebook.com/v2.8/"+req, {'access_token':token})
    return  r
    
req="7729761102/feed?fields=comments{message,from},from,message&limit=100"
r=fb_request(req)
result = r.json
def get_data(req):
    data=[]

   # posts = graph.get_object("7729761102"+req)

    while True:
        try:
            time.sleep(1)
            # Perform some action on each post in the collection we receive from
            # Facebook.
          #  some_action(posts)
            data.extend(posts['data'])
            # Attempt to make a request to the next page of data, if it exists.
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            print "done"
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break
    return data
    






















#Tutorial 2
#making many requests for many people in a group
#grouping
#getting top people 

#top people commenting

#Tutorial 3

