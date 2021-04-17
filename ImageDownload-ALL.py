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
img_path = "./picture/"
if not os.path.exists(img_path):
    os.makedirs(img_path)

#Convert Dict to pdframe
panda_data = pd.DataFrame(data.items(), columns=['recipeID', 'Value'])
#Convert pdframe to list
list_dict = []
for index, row in panda_data.iterrows():
    list_dict.append(row["Value"])

for item in list_dict:
  #Obtain recipe ID
  recipe_ID = item['recipe_ID']
  # Step List
  instructions_dict = item['instructions']
  step_num = 0
  for i in instructions_dict:
    #Obtain StepNumber
    step_num = step_num + 1
    #Download Images
    try:
        response = requests.get(i['img_link'])
        file = open(img_path+recipe_ID+"_"+str(step_num)+".jpg", "wb")
        file.write(response.content)
        file.close()
    except:
        continue
