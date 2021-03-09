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
