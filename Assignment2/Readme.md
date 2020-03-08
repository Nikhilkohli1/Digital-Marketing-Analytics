# E-commerce Online Sales Marketing Insights 


Dashboard Insights video link - https://youtu.be/XCnGIvJ4QL8

CLAAT document link - https://docs.google.com/document/d/1vqdOtfYADITw0em9_nDmxXO1-Eci66TrX2nyiMPHoNk/edit?usp=sharing

CLAAT Preview Link - https://codelabs-preview.appspot.com/?file_id=1vqdOtfYADITw0em9_nDmxXO1-Eci66TrX2nyiMPHoNk#0

Description - 

In this assignment, we are provided with a sample dataset and asked to analyze and build an analytical dashboard as a Proof-of-concept to illustrate the value of data driven analytics.

The themes to be considered include:
• Pricing
• Promotion
• Search
• Recommendations


We will analyze the data using tools (Pandas, xsv, Trifacta) and build a dashboard using Salesforce Einstein analytics. 

The dataset we are provided can be download from the below link - 
https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store

It contains behavior data for two months (October and November 2019) from a large multi-category online store.
Each row in the file represents an event. All events are related to products and users. Each event is like many-to-many relation between products and users.

Feature Information - 

event_time  - Time when event happened at (in UTC).

event_type - Events can be:

view - a user viewed a product
cart - a user added a product to shopping cart
purchase - a user purchased a product

product_id - ID of a product

category_id - Product's category ID

category_code - Product's category code

brand - brand name

price - Float price of a product

user_id - Permanent user ID.

user_session - Temporary user's session ID. 


You can Run the Steps described below to View/Replicate the outcome of the tasks. 

1. Download the datasets for Oct & Nov 2019 from the link 

https://www.kaggle.com/mkechinov/ecommerce-behavior-data-from-multi-category-store

The files are huge to we can sample it using XSV tool to take a sample subset of the data. 
We will be trying 3 tools for Data Wrangling viz - XSV, Pandas, Trifacta 

2. Install the XSV tool if not already done. 
   https://github.com/BurntSushi/xsv

3. Run the XSV commands to Sample the dataset and other Wrangling operations like Filtering, Joining, Slicing, Search, cleaning etc. 
Follow the Claat document to see the commands or you can also find this information on the github link for XSV. 

4. Now lets move over to Pandas - 

Run the Below Notebooks in the same order to do Data Wrangling and Generate a Final cleaned output. These notebooks are available in Pandas folder. 

A. Data_V1_Top_Brands_Nov_2019.ipynb - 
Missing value Analysis & Imputing for Nov 2019 file 

B. Data_V1_Top_Brands_Oct_2019.ipynb - 
Missing value Analysis & Imputing for Oct 2019 file

C. Data_V1_Top_Brands_Concat_Oct_Nov.ipynb - 
Concatenate the 2 files generated above and samples the output to be under 2.5 lakh rows 
(As there is a limit on uploading data in Trifacta(100 mb) and Salesforce(2.5 lakh rows))

D. ADM_Assign2_Pandas_Wrangling_&_EDA.ipynb - 
Generate new cols from existing ones like Event hour, Date, Category, Subcategory, Day of Week,
Timezone etc. Applied some Wrangling operations like filtering, regex, Aggregate, Groupby. 

We also did some Visualisations using Matplotlib in python. 
We also generated a new dataset for User Demography Information (State and User Score)

5. After pandas, we tried Trifacta - 
Create a flow and import the dataset saved in step 4.C & 4.D '2019_Ecommerce_Sales_Data_Trifacta.csv' & '2019_user_details.csv'
You can also download these data files from Trifacta>Input folder in the repo. 

We created the recipe for Transformation to Wrangle the data to make it ready for Data Visualisations in Salesforce. 
'2019_Ecomm_Sales_Data_Trifacta.wrangle' this file under Trifacta folder has all the recipe transformations. 

It joins the 2 files in the flow and then wrangles the data using the Recipe created.

6. Use the output generated - '2019_Ecommerce_Sales_Data_Salesforce.csv'
We uploaded this to salesforce Einstein Analytics and Created An App > Dataset > DataFlow > Dashboard 

We created 5 Dashboards for the below Themes - 
• Pricing
• Promotion
• Search
• Recommendations
• Monthly Pricing and Insights

![Monthly pricing Insights](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment2/Monthly_Pricing_Sales_Insights.png)

![Recommendations](https://github.com/Nikhilkohli1/Digital-Marketing-Analytics/blob/master/Assignment2/Ecommerce_Sales_Dashboard%20(1).png)



You can generate your own insights as well based on your understanding of the data. Or you can also generate/use additional datasets 
which might have details for promotional campaigns. These insights and Datasets can be further used to build 
prediction models for forcasting LTV, prices, Sales, Recommendations etc. 






