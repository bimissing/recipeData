#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import pandas as pd
import requests
import os
import csv
import numpy as np
import shutil, os
import random
from shutil import copy2

#Read 1-DimensionFeature CSV file
# with open('/Users/admin/PycharmProjects/fileProcessing/1-DimensionFinalNew1origin.csv','r') as csvFile:
#     reader = csv.reader(csvFile)
#     result = [row for row in reader]

#Read JSON file
with open('./recipeData.json','r') as f:
  data = json.load(f)


#Convert Dict to pdframe
pdData = pd.DataFrame(data.items(), columns=['recipeID', 'Value'])
#Convert pdframe to list
listDict = []
for index, row in pdData.iterrows():
    listDict.append(row["Value"])

FileNameList = []
imgLinkList = []

for item in listDict:
  #Obtain recipe ID
  recipeID = item['recipeID']
  # Step List
  instructionsDict = item['instructions']

  stepNum = 0
  for i in instructionsDict:
    #Download Images
    try:
        FileName = recipeID + "_" + str(stepNum)
        FileNameList.append(FileName)

        imgLink = i['imgLink']
        imgLinkList.append(imgLink)

        stepNum = stepNum + 1
    except:
        continue

LinkFileList = list(zip(FileNameList, imgLinkList))
print(LinkFileList[0])


#Read 1-DimensionFeature CSV file
df1 = pd.read_csv("/Users/admin/PycharmProjects/fileProcessing/1-DimensionFinalNew1originSub.csv", low_memory=False)
df2 = pd.DataFrame(LinkFileList)
df2.columns = ["FileName","ImgLink"]
# df1['FileName']=df1['FileName'].astype(int)
# df2['FileName']=df1['FileName'].astype(int)

#Merge LinkList and FileInfoList with 1-Dimension feature
df3 = pd.merge(df1, df2, how='inner', on=['FileName'], sort='Group')
df4 = df3.drop_duplicates()
df4.to_csv("ImageInfo.csv",index=False)


#Download the images to each subsets
def createSubsetCategoriesList(categories,subsets):
    with open('ImageInfo.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        result = [row for row in reader]
    print(result[1])
    print(len(categories) + 1)

    for m in range(1, len(subsets) + 1):
        # print(m)
        count = 0
        for n in range(1, len(categories) + 1):
            # print(n)
            for i in range(1, len(result)):
                if result[i][5] == str(n) and result[i][6] == str(m):
                    imageLink = result[i][7]
                    # print(imageLink)
                    # count = count + 1
                    imgpath = "./subsets/"+str(m)+"/"+str(n)+"/"
                    if not os.path.exists(imgpath):
                        # os.mkdir(imgpath)
                        os.makedirs(imgpath)
                    try:
                        response = requests.get(imageLink)
                        file = open(imgpath+result[i][2]+".jpg", "wb")
                        file.write(response.content)
                        file.close()
                    except:
                        continue
            # print(count)

subsets=[1,2,3]
categories=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
createSubsetCategoriesList(categories,subsets)