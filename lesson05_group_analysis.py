import pickle
import pandas as pd 
import string
from operator import itemgetter
loaded_data= pickle.load(file=open("buyandsell_group.pkl"))

df2 = pd.io.json.json_normalize(data=loaded_data)

