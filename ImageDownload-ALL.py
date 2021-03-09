#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import pandas as pd
import requests
import os

#Download all the images in JSON file

#Read JSON file
with open('./recipeData.json','r') as f:
  data = json.load(f)
print(data)

#Create Image saving path
imgpath = "./picture/"
if not os.path.exists(imgpath):
    # os.mkdir(imgpath)
    os.makedirs(imgpath)

#Convert Dict to pdframe
pandaData = pd.DataFrame(data.items(), columns=['recipeID', 'Value'])
#Convert pdframe to list
listDict = []
for index, row in pandaData.iterrows():
    listDict.append(row["Value"])

for item in listDict:
  #Obtain recipe ID
  recipeID = item['recipeID']
  # Step List
  instructionsDict = item['instructions']
  stepNum = 0
  for i in instructionsDict:
    #Obtain StepNumber
    stepNum = stepNum + 1
    #Download Images
    try:
        response = requests.get(i['imgLink'])
        file = open(imgpath+recipeID+"_"+str(stepNum)+".jpg", "wb")
        file.write(response.content)
        file.close()
    except:
        continue