# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 03:06:48 2017

@author: Nour
"""

import pickle
import pandas as pd 

#loaded_data= pickle.load(file=open("buyandsell_group.pkl"))

music_df = pd.io.json.json_normalize(data=loaded_data)
print "hi"

df_group.head()


music_df['created_time']=pd.DataFrame (pd.to_datetime(music_df.created_time))

y=music_df.iloc[0]
type(y['created_time'])



#PLOT BY MONTH

grouped_by_months=music_df['id'].groupby(music_df.created_time.dt.month).count()
fig=grouped_by_months.plot(kind="bar", legend=True,title="Posts per Month")

fig.figure

#PLOT BY DAY
grouped_by_months=music_df['id'].groupby(music_df.created_time.dt.day).count()
fig=grouped_by_months.plot(kind="bar", legend=True,title="Posts per Month")

fig.figure


#PLOT BY Year
grouped_by_months=music_df['id'].groupby(music_df.created_time.dt.year).count()
fig=grouped_by_months.plot(kind="bar", legend=True,title="Posts per Month")

fig.figure