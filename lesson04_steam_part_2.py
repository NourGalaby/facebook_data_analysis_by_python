# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 03:06:48 2017

@author: Nour
"""

import pickle
import pandas as pd 

loaded_data= pickle.load(file=open("steam_data.pkl"))

comments_likes_df = pd.io.json.json_normalize(data=loaded_data)


loaded_data= pickle.load(file=open("steam_data2.pkl"))
steam_data=pd.io.json.json_normalize(data=loaded_data)

loaded_data= pickle.load(file=open("steam_data.pkl"))
steam_data1=pd.io.json.json_normalize(data=loaded_data)
head=steam_df.head()-