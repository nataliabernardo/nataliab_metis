## Project 2 - Predicting the Success of a Recipe

Project 2 was an opportunity for us to learn web scraping using BeautifulSoup and Selenium and supervised machine learning techniques.
My project was about predicting the success of a recipe based on the ingredients and nutrition information. As a fan of the good food, I have always been curious on which elements make the dishes better. For this purpose, I chose to analyze the Epicurious.com recipes and their ratings.

### Data Scraping

I used BeautifulSoup for this task. Epicurious.com has an organized html source code structure, so it was not a big challenge. I automatized the search for recipes (filtered by lunch and dinner meals) and scrapping. Since it involved parsing hundreds of results pages and thousands of recipes, I made the scrapping stage in 8 batches, so I could avoid the risk of losing information. 

### Feature Selection

For the target variable, I chose to measure the Success score by the rating combined with the percentage of people that said that would make that recipe again. It seems more realistic than using purely ratings.

### Exploratory Data analysis

### Results

### Final Thoughts
