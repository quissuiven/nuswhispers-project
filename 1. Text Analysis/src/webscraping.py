# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:02:41 2019

@author: Hong.Wen.Tai
"""

import requests
import pandas as pd
import numpy as np
from time import sleep

#create dataframe to store variables. shape of dataframe should be greater than no of urls (44438)
info = ["confession_id", "content", "created_at", "fb_like_count", "fb_comment_count", "facebook_information"]
array = np.zeros(shape=(44400,6))         
df = pd.DataFrame(array, columns = info)

offset_count = 0          
while offset_count < 44400:                 
    
    #send a request to url and store response in an object. url is determined by offset_count
    url = "https://nuswhispers.com/api/confessions/recent?count=5&offset=%d&timestamp=1571749717" %(offset_count)
    response = requests.get(url)
    infinitedata = response.json()
    
    #extract each item in info from the dictionary object
    count = 0
    for j in range(offset_count, offset_count + 5):
        for i in info:
            if i == "facebook_information":
                df[i].iloc[j] =  str(infinitedata["data"]["confessions"][count][i])      #use str() since can't store dictionary into Pandas Dataframe
            else:
                df[i].iloc[j] =  infinitedata["data"]["confessions"][count][i]
        count += 1
                 
    #add 5 to offset_count to retrieve the next url
    offset_count += 5
    
    #suspend request periodically so that won't send too many requests in a short period of time
    #if offset_count == 10000 or offset_count == 20000 or offset_count == 30000 or offset_count == 40000:
    #    sleep(60)
        
    
#export dataframe to excel file
filename = 'nuswhispers_cleaned.csv'
df.to_csv(filename,index=False)
print('Saved file: ' + filename)

