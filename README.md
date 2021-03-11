# recipeData

### recipeData.json:
Crawlered from https://www.haodou.com/recipe

Recipe information includes recipeName, recipeID, brief descriptions, ingredients, seasonings, instructions and tips.

Each instruction contains a description and link of corresponding image.

### ImageInfo.csv:
Image information contains Recipe_id, totalNumOfStep, FileName, Step_num, Nper (relative position), Category_num, SubsetNum, ImgLink

#### 3 subsets:
Beginning Stage Subset, Intermediate Stage Subset, Finishing Stage Subset

Split based on the relative position of steps in the corresponding recipe.

#### 20 categories:
Potato, ginger, onion, pork, shrimp, chicken, corn, carrot, eggplant, shallot, tofu, spinach, sauce, chili, bread, dough, fish, egg, cucumber and soybean.


### ImageDownload-ALL.py
Download all the images in recipeData.json.

### ImageDownload-SUBSETS.py
Download images by per subsets per categories.
