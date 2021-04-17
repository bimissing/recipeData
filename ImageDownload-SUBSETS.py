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
def create_subset_categories_list(categories,subsets):
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
                    image_link = result[i][7]
                    # print(imageLink)
                    # count = count + 1
                    img_path = "./subsets/"+str(m)+"/"+str(n)+"/"
                    if not os.path.exists(img_path):
                        # os.mkdir(imgpath)
                        os.makedirs(img_path)
                    try:
                        response = requests.get(image_link)
                        file = open(img_path+result[i][2]+".jpg", "wb")
                        file.write(response.content)
                        file.close()
                    except:
                        continue
            # print(count)

subsets=[1,2,3]
categories=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# 1 Potato, 2 ginger, 3 onion, 4 pork, 5 shrimp, 6 chicken, 7 corn, 8 carrot, 9 eggplant, 10 shallot, 11 tofu, 12 spinach, 13 sauce, 14 chili, 15bread, 16 dough, 17 fish, 18 egg, 19 cucumber and 20 soybean.
create_subset_categories_list(categories,subsets)
