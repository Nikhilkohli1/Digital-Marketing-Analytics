# Olist Marketing Analytics: RFM Modeling, Customer Segmentation & Upselling, Targeted Recommendations


Olist Streamlit Analytics Dashboard - https://olist-streamlit-dashboard.herokuapp.com/

Recommendation Webapp - https://olist-marketing-analytics.herokuapp.com/
(Customer ID for Referene :
41412 - Cross Selling (ALS Recommendation)
30369 - Doc2Vec (Loyal Customer Segment)
1000000 - Popular Recommendation (New Customer)
28880 - Upselling Highest Rated (Big Spenders and VVIP)
)

Marketing Dashboard - https://prod-useast-a.online.tableau.com/#/site/mohodhruda/views/OlistMarketingDashboard/Dashboard

(Credentials to access Marketing Dashboard- 
Username: mohod.h@husky.neu.edu
Password : Tableau1!)

CLAAT Document - https://docs.google.com/document/d/1BoSlam9Pp4LPUwb88HmeilAvCu6RH2-b8ECv4c8M0NM/edit#heading=h.ax8bqte2btx2

CLAAT Preview Link - https://codelabs-preview.appspot.com/?file_id=1BoSlam9Pp4LPUwb88HmeilAvCu6RH2-b8ECv4c8M0NM#0

## Olist Marketing Analytics 

A Data Driven Algorithmic Marketing system for brazil’s biggest online marketplace Olist, to segment customers, RFM & Uplift Modeling, Identify Upselling and Cross Selling opportunities using Targeted Recommendations.
![Olist](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/Images/marketing-analytics-featured-image-1.jpg)

Marketing Analytics at Olist helps in measuring, managing and analyzing marketing performance to maximize its effectiveness and optimize ROI. Understanding Marketing analytics allows Olist to minimize wasted web marketing dollars by attributing budget to the targeted campaign, missed opportunities by not being able to show recommendations personalized as per the user's preferences. 

![geo](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/Images/mapplot.png)

## Approach

1. We started with EDA and Trend Analysis of Products and Customers to get insights for a business Analyst. 
2. Then we Segmented customers into specific clusters based on Cohort Analysis, RFM Modeling using their purchasing behavior. Measure MOCP/MICP (Marketing Influenced Customer Percentage)
3. Then we used uplift/persuasion modeling to identify which customer needs treatment and identify Upselling & Cross Selling Opportunities
4. Predict Customer Lifetime value (LTV)
5. Personalized Recommendations using Implicit feedback in the form of customer’s past purchases and Explicit feedback in the form of their Product Reviews. We have used Alternative Least Squares(ALS) and Doc2Vec for creating 2 different control groups to which Recommendations will be provided. A new user will see the popular recommendations, and using Segmentation, we will identify who are Big Spenders and will Upsell them using Highest rated product recommendations. 
6. We have created 3 different personas for front end and presented the outcomes as a Marketing dashboard as well as a fully deployed Webapp.

## Personas 

1. Higher Management Executives - Marketing Dashboard
• To get insights on a high level cohorts and Metrics for Revenue by Products, day of week and month. 
• To look at overall Customer Segments to see the health of marketing.  
![Dash1](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/Images/Dash%201.JPG)

2. Marketing Data Scientist & Automated System:
• To form promotion strategies based on Marketing Insights and Uplift
• Recommend products to customers based on their liking along with any Upselling and Cross Selling opportunities
• Optimize the Marketing Funnel to boost Revenue, offer Targeted Recommendations
![Dash2](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/Images/StreamDash1.PNG)


3. End Users or Potential Customers:
• Explore products recommended by the system
• Receive promotions based on their loyalty, demography
• Explore Products which are similar to what they are about to buy or have purchased previously
![Dash3](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/Images/Heroku2.PNG)

## Customer Segmentation and RFM Modeling 

Using RFM anaylsis and K-means Clustering, we created the below Clusters or segments of customers to further give targetted recommendation to them. 

1. Potential Loyalists —
High potential to enter our loyal customer segments, why not throw in some freebies on their next purchase to show that you value them!

2. Needs Attention —
Showing promising signs with quantity and value of their purchase but it has been a while since they last bought sometime from you. Let's target them with their wishlist items and a limited time offer discount.

3. Hibernating Almost Lost —
Made some initial purchases but have not seen them since. Was it a bad customer experience? Or product-market fit? Let's spend some resources building our brand awareness with them.

4. Lost Customers —
Poorest performers of our RFM model. They might have gone with our competitors for now and will require a different activation strategy to

![RFM](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/3.%20RFM%20Modeling%20%26%20Customer%20Segmentation/Segmentation.PNG)


## Recommendation Systems  

Recommender systems are algorithms aimed at suggesting relevant items to users (items being movies to watch, text to read, products to buy or anything else depending on industries).

Recommender systems are really critical in some industries as they can generate a huge amount of income when they are efficient or also be a way to stand out significantly from competitors. As a proof of the importance of recommender systems, we can mention that, a few years ago, Netflix organised a challenge (the "Netflix prize") where the goal was to produce a recommender system that performs better than its own algorithm with a prize of 1 million dollars to win.

![Reco](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/5.%20Recommendation%20System/Heroku1.PNG)

We will be using below approach to Recommend products - 
 
1. Recommendation for Potential Loyalists and Other - 
ALS (Alternating Least Squares) is an implicit recommendation algorithm to make a recommendation of products and product categories to the users. ALS is an iterative optimization process where for every iteration it tries to arrive closer and closer to a factorized representation of the original data.

2. Recommendation for Loyal Customers who buys Products Frequently and Recently -
Customer2Vec is a good method for these kinds of users. As these customers usually repeat their orders and buys frequently. We learn a semantic representation for Customers using their previous purchase history.

We learn good semantic representations for customers (users) from transactional data using doc2vec. Each customer is a document, orders are sentences, and products are words. We also compare Customer2Vec with the baseline

3. For Big Spenders - 
We use Upselling to recommend products to Big Spenders and VVIP customers using Highest Rated and High end prodcuts. 

4. For new Customers - 
We show Popular Products by current month for new customers. 


## Dashboards - 

![Streamlit2](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/Images/Dash3.JPG)

![Streamlit1](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/Images/StreamDash1.PNG)

![Social1](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/Images/streaming.png)

![Social](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Olist%20Marketing%20Analytics%20Project/Images/StreamDash3.PNG)





