## Project 2 - Predicting the Success of a Recipe

Project 2 was an opportunity for us to learn web scraping using BeautifulSoup and Selenium and supervised machine learning techniques.
My project was about predicting the success of a recipe based on the ingredients and nutrition information. As a fan of the good food, I have always been curious on which elements make the dishes better. For this purpose, I chose to use a multivariable linear regression model on Epicurious.com recipes.

### Data Scraping

I used BeautifulSoup for this task. Epicurious.com has an organized html source code structure, so it was not a big challenge. I automatized the search for recipes (filtered by lunch and dinner meals) and scrapping. Since it involved parsing hundreds of results pages and thousands of recipes, I made the scrapping stage in 8 batches, so I could avoid the risk of losing information. 

 

### Feature Selection

 

For the target variable, I chose to measure the Success score by the rating combined with the percentage of people that said that would make that recipe again, following the formula. 

Success score = rating  x Make_it_again



It seems more realistic than using purely ratings.



 

As features, 2 types of information were used:
"	Nutrition data: calories, carbohydrates, sodium, protein, etc per serving
"	Key ingredients: + 300 categorical features

The nutrition data right skewed, so I transformed them to log, so they had a better distribution. 

 

For the ingredients, since there were many, I used the Recursive Feature Elimination (RFE) for choosing the 50 most important ingredients that explain the ratings. The RFE ranks the predictors based on their contribution to the model.

### Exploratory Data analysis

In this stage, I realized that a linear regression was not the most appropriate model for analyzing ingredients of a recipe. This method assumes that features are independent, however, the success of a recipe is a result of the combination of flavors, therefore, the interaction between ingredients should be taken into consideration.

In whatever way, the linear regression model performed well and it was possible to get some insights from its results. I used train/test split method from sklearn to divide the data in 70% train and 30% test. Below is the summary of the the OLS model.







### Results

### Final Thoughts
