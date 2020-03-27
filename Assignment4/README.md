# Recommendation Systems - xDeepFM & Customer2Vec



CLAAT Document - https://docs.google.com/document/d/18zaAjqPpA-ewZaGBHoPhRu6nFrp9PDiM-q-zhjWkNgM/edit#heading=h.ax8bqte2btx2

CLAAT Preview Link - https://codelabs-preview.appspot.com/?file_id=18zaAjqPpA-ewZaGBHoPhRu6nFrp9PDiM-q-zhjWkNgM#0

Description - 


## Recommendation Systems  

Recommender systems are algorithms aimed at suggesting relevant items to users (items being movies to watch, text to read, products to buy or anything else depending on industries).

Recommender systems are really critical in some industries as they can generate a huge amount of income when they are efficient or also be a way to stand out significantly from competitors. As a proof of the importance of recommender systems, we can mention that, a few years ago, Netflix organised a challenge (the "Netflix prize") where the goal was to produce a recommender system that performs better than its own algorithm with a prize of 1 million dollars to win.

![xDeepFM](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment4/Images/model1.PNG)

## Extreme Deep Factorization


xDeepFM is a deep learning based algorithm for implicit and explicit feedback with user/item features
This is a hybrid approach where it tries to learn both implicit and explicit features.

All examples of the hybrid category use Deep Neural Networks to learn implicit bitwise feature interactions. They differ in how the high order feature interactions are learned.

#### xDeepFM comprises of 3 parts:

The linear model ( Directly work on top of raw input features )
Plain DNN (Works on top of dense feature embeddings)
CIN (Works on top of dense feature embeddings)
We implement this on the 2 sample datasets first. (Synthetic dataset and Cretio)

Then we created a sample dataset for Snacks which contains the CTR information and the xDeepFM algorithm learns the implicit feedback to predict whether a user will interact with a particular campaign or not.


CTR Click Prediction data (Faker + Criteo CTR)


![Dataset](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment4/Images/ctr.png)

This dataset is based on Click through rate dataset. We have columns like Customer name, Campaign details with categorical features related to the ad shown to users, user details and whether they clicked an Advertisement for a product or not. This will help us in recommending Products/Campaigns/Ads to customers that they are more likely to click and convert.


## Customer2Vec


We learn good semantic representations for customers (users) from transactional data using doc2vec. Each customer is a document, orders are sentences, and products are words. We also compare Customer2Vec with the baseline representations obtained using k-means on manually designed features.

![Data](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment4/Images/customer2vec.png)


The data we used here is based on Instacart market basket data. It has information like product details, departments etc. Later we create the list of user journeys in terms of orders made by a user in chronological order. This will help us in recommending products to customers which they are most likely to add to their cart or just continue their subscription for a particular snack category. It can also help us in retaining customers who can churn in future.



### Streamlit Dashbaord -

We also create a Dashbaord using Streamlit to summarize our insights and model outcomes. 

![Dashboard1](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment4/Images/search.PNG)

![Dashboard2](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment4/Images/xDeepfmmodel.PNG)


