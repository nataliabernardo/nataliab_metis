## Project 2 - Predicting the Success of a Recipe

Is it possible to predict the success of a recipe based on its ingredients independently? The answer is no. Heston Blumenthal, the father of food pairing, needs at least 2 combined ingredients to make a special meal, however, it was possible to get good insights from the analysis.

<p align="center"> <img src="https://github.com/nataliabernardo/nataliab_metis/blob/master/Project_2/images/srep00196-f2.jpg" width="60%"></p>

Project 2 was an opportunity for us to learn web scraping using BeautifulSoup and Selenium and Supervised Machine Learning techniques. My project was about predicting the success of a recipe based on the main ingredients and nutrition information. As a fan of the good food, I have always been curious on which elements make the dishes better. For this purpose, I chose to use a multivariable linear regression model on Epicurious.com recipes.

### Data Scraping

I used BeautifulSoup for this task. Epicurious.com has an organized html source code structure, so it was not a big challenge. I automatized the search for recipes (filtered by lunch and dinner meals) and scrapping. Since it involved parsing hundreds of results pages and thousands of recipes, I made the scrapping stage in 8 batches, so I could avoid the risk of losing information. 


### Feature Selection

 

For the target variable, I chose to measure the Success score by the rating combined with the percentage of people that said that would make that recipe again. 

![](https://github.com/nataliabernardo/nataliab_metis/blob/master/Project_2/images/Screen%20Shot%202018-02-26%20at%209.06.42%20PM.png)


It seems more realistic than using purely ratings and has a better distribution.

 <p align="center"> <img src="https://github.com/nataliabernardo/nataliab_metis/blob/master/Project_2/images/Picture1.png" width="60%"></p>

As features, 2 types of information were used:
*	Nutrition data: calories, carbohydrates, sodium, protein, etc per serving
*	Key ingredients: + 300 categorical features

As the nutrition data is right skewed (as in the example below), I transformed them to log, so they had a better distribution.  

<p align="center"> <img src="https://github.com/nataliabernardo/nataliab_metis/blob/master/Project_2/images/Picture2.png" width="65%"></p>
 
For the ingredients, since there were many, I used the Recursive Feature Elimination (RFE) for choosing the 50 most important ingredients that explain the ratings. The RFE ranks the predictors based on their contribution to the model.

### Exploratory Data analysis

In this stage, I realized that a linear regression was not the most appropriate model for analyzing ingredients of a recipe. This method assumes that features are independent, however, the success of a recipe is a result of the combination of flavors. The interaction between ingredients should be taken into consideration.

In whatever way, the linear regression model performed well and it was possible to get some insights from its results. I used train/test split method from sklearn to divide the data in 70% train and 30% test. 

When modelling  with all of my features my model came out with an r-squared of 0.94 and a mean squared error of 0.59, which was better than expected. In an attempt to reduce the mean squared error, I excluded the features whose p-value were higher than 0.05 (relationship between that feature and the rating is not statistically significant). The r-squared increased to 0.95, meaning my model could account for 95% variance in the score, and a mean squared error of 0.57! Below is the summary of the resulting OLS model.

<p align="center"> <img src="https://github.com/nataliabernardo/nataliab_metis/blob/master/Project_2/images/Picture3.png" width="55%"></p>

### Results

It resulted that unhealthier, such as calories, components have a positive coefficient,meaning that they lead to higher ratings.

<p align="center"> <img src="https://github.com/nataliabernardo/nataliab_metis/blob/master/Project_2/images/Screen%20Shot%202018-02-26%20at%209.55.59%20PM.png?raw=true" width="80%"></p>

Regarding the ingredients, if you look closer to the ones that most impact the ratings, you come to the conclusion that they are mostly not main ingredients, but flavor additions to the recipes!

<p align="center"> <img src="https://github.com/nataliabernardo/nataliab_metis/blob/master/Project_2/images/Screen%20Shot%202018-02-26%20at%208.46.43%20PM.png?raw=true" width="80%"></p>


### Final Thoughts
