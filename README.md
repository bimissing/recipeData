This repo provides python source code for creating mini-ImageNet dataset from ImageNet and the utils for generating batches during training. This repo is related to our work on few-shot learning: [Meta-Transfer Learning](https://github.com/y2l/meta-transfer-learning-tensorflow).


## Summary

* [About MIRecipe](#about-MIRecipe)
* [Requirements](#requirements)
* [Datasets](#datasets)


## About MIRecipe
**MIRecipe** consists of 239,973 instructional images in recipes. Each recipe item includes recipeName, recipeID, brief descriptions, ingredients, seasonings, instructions (both text and image) and tips.

It consists of 26,725 recipes in Chinese, which include 155,345 multimedia steps (both text and image)  in total.


## Requirements

- Python 3.x
- pytorch 0.4+
- numpy

## Datasets

### Usage
First, you need to download the image by per subsets per categories from `ImageDownload-SUBSETS.py`. 
If you need all the recipe images, you could download them from `ImageDownload-ALL.py`

### Data Collection
#### recipeData.json & recipeData-new1.json:
Our recipe data is crawlered from https://www.haodou.com/recipe .

Recipe information in our dataset includes **recipeName, recipeID, brief descriptions, ingredients, seasonings, instructions and tips**.

Each instruction contains a **text description and link of corresponding image**.

#### ImageInfo.csv:
Image information contains Recipe_id, totalNumOfStep, FileName, Step_num, Nper (relative position), Category_num, SubsetNum, ImgLink

### 3 subsets:
Beginning Stage Subset, Intermediate Stage Subset, Finishing Stage Subset

Split based on the relative position of steps in the corresponding recipe.

### 20 categories: (In order)
Potato, ginger, onion, pork, shrimp, chicken, corn, carrot, eggplant, shallot, tofu, spinach, sauce, chili, bread, dough, fish, egg, cucumber and soybean.


## Train the model
### Food Subset-Based Recognition Model Selector
If you want to train the model, just run `python3 trainRESNET.py`. You may need to change the configurations in `trainRESNET.py`. The parameter 'DIR_TRAIN_IMAGES' is the category list of train and 'DIR_TEST_IMAGES' is the category list of test. 'IMAGE_PATH' is the path of the image folder. During training, the checkpoint file will be saved.


