This repo provides python source code for creating mini-ImageNet dataset from ImageNet and the utils for generating batches during training. This repo is related to our work on few-shot learning: [Meta-Transfer Learning](https://github.com/y2l/meta-transfer-learning-tensorflow).


## Summary

* [About MIRecipe](#about-MIRecipe)
* [Requirements](#requirements)
* [Datasets](#datasets)


## About MIRecipe
**MIRecipe** consists of 239,973 instructional images in recipes. Each recipe item includes recipeName, recipeID, brief descriptions, ingredients, seasonings, instructions (both text and image) and tips.

It consists of 26,725 recipes in Chinese, which include 239,973 multimedia steps (both text and image)  in total.


## Requirements

- Python 3.x
- pytorch 0.4+
- numpy

## Datasets
### Conceptual Example of recipes on website:

<img src="https://github.com/bimissing/recipeData/blob/main/IMG/exampleMM.png" width="50%" height="50%">

Structure of multimedia instructional recipe data.  Recipe instruction is a sequence of cooking steps, each of which consists of a text description and an associated image.

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

### Dataset Statistics:
<img src="https://github.com/bimissing/recipeData/blob/main/IMG/stats001.png" width="40%" height="40%">

<img src="https://github.com/bimissing/recipeData/blob/main/IMG/stats002.png" width="40%" height="40%">

<img src="https://github.com/bimissing/recipeData/blob/main/IMG/stats003.png" width="40%" height="40%">

Figures above show the dataset statistics. Most recipes include more than four and less than 15 cooking steps, and the mode of the distribution of the number of cooking steps is 7. 

Each recipe on Haodou site has two ingredient lists, main ingredients, and side ingredients. The 3rd graph shows the distribution of the number of main ingredients and side ingredients separately.  Side ingredients include salt, oil, and so on, but it also often includes foodstuffs that require cooking processes, such as garlic and ginger.  Side ingredients sometimes include even carrots and so on, when they are not the main ingredients of the recipe.  Therefore, we use both main ingredient lists, and side ingredient lists as the candidate lists of foodstuffs omitted in the text instructions.

### 3 subsets:
Beginning Stage Subset, Intermediate Stage Subset, Finishing Stage Subset

Split based on the relative position of steps in the corresponding recipe.

### 20 categories: (In order)
Potato, ginger, onion, pork, shrimp, chicken, corn, carrot, eggplant, shallot, tofu, spinach, sauce, chili, bread, dough, fish, egg, cucumber and soybean.

<img src="https://github.com/bimissing/recipeData/blob/main/IMG/Division%20of%2020%20class%20of%20food.png" width="60%" height="60%">

The statistics of the final training and test sets used in our experiment is shown in the table above. 

In this table, from a vertical perspective, thenumber of images in each subset of each class is relatively averagedistribution. From a horizontal perspective of this table, the imagevolume of seasonings such as ginger and shallot classes are higherin each subset.

## Train the model
### Food Subset-Based Recognition Model Selector
If you want to train the model, just run `python3 train.py` (vgg16 version) (can change the parameter to train as ResNet50 architecture or others). You may need to change the configurations in `train.py`. The parameter 'DIR_TRAIN_IMAGES' is the category list of train and 'DIR_TEST_IMAGES' is the category list of test. 'IMAGE_PATH' is the path of the image folder. During training, the checkpoint file will be saved.


