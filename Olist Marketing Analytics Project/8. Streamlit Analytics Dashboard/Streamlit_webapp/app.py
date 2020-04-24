
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
import pickle
import plotly.express as px
import json
import plotly.figure_factory as ff
import time

from PIL import Image
import plotly.graph_objects as go


import glob
from IPython.display import display, HTML
from tqdm import tqdm_notebook as tqdm
from sklearn import preprocessing

import twitter
import json
from urllib.parse import unquote
import credentials 
#import twitter
#import json
from urllib.parse import unquote


import matplotlib.pyplot as plt
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import os

import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


def configure_plotly_browser_state():
    import IPython
    display(IPython.core.display.HTML('''
        <script src="/static/components/requirejs/require.js"></script>
        <script>
          requirejs.config({
            paths: {
              base: '/static/base',
              plotly: 'https://cdn.plot.ly/plotly-latest.min.js?noext',
            },
          });
        </script>
        '''))


#os.chdir(r'N:\Olist Marketing Analytics\Streamlit_webapp')

Olist= pd.read_csv('./data/Olist_Master.csv')
hashtag = pd.read_csv('./data/hashtags.csv')
# converting date columns to datetime
date_columns = ['shipping_limit_date', 'review_creation_date', 'review_answer_timestamp', 'order_purchase_timestamp', 'order_estimated_delivery_date']
for col in date_columns:
    Olist[col] = pd.to_datetime(Olist[col], format='%Y-%m-%d %H:%M:%S')

#Olist = Olist[['order_id','product_id', 'seller_id' ,'price', 'payment_type', 'customer_city', 'customer_state']]
#Olist.head()


st.title("Olist Analytics Dashboard - Marketing Matters!")

st.markdown("""
<style>
body {
    color: #fff;
    background-color: #0A3648;
}
</style>
    """, unsafe_allow_html=True)

# #071433   0A3648

menu=["Product & Customer Behaviour Analysis", "Customer Segmentation & LTV", "Social Media & Geography Analysis"]
choices = st.sidebar.selectbox("Select Analytics Dashboard",menu)

if choices == 'Product & Customer Behaviour Analysis':
    st.subheader('Product & Customer Behaviour Analysis')
    st.sidebar.success("Knowing who your Customers are is great, but knowing how they behave is even better.")

    # creating a purchase day feature
    sales_per_purchase_month = Olist.groupby(['order_purchase_month', 'order_purchase_mon', 'order_purchase_day'], as_index=False).payment_value.sum()
    sales_per_purchase_month = sales_per_purchase_month.sort_values(by=['order_purchase_month'], ascending=True)
    
    #st.write('Sales Each Month & Each Day of Week')
    st.markdown('Sales by **_Month_ _&_  _Day_ _of_ Week**.')

    df = sales_per_purchase_month
    fig = px.line(df, x="order_purchase_mon", y="payment_value", color='order_purchase_day', title='Sales Each Month & Each DayofWeek')

    fig.update_layout(
        title="Sales Each Month & Each DayofWeek",
        xaxis_title="Months",
        yaxis_title="Sales(in $$)",
        font=dict(
            family="Courier New, monospace",
            size=15,
            color="#7f7f7f"
        )
    )
    #ig.show()
    #st.line_chart(fig)
    st.write(fig)
    
    
    
    Olist['review_dayofweek'] = Olist.review_answer_timestamp.apply(lambda x: x.dayofweek)
    Olist['review_day'] = Olist['review_dayofweek'].map({0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'})
    Olist['review_month'] = Olist.review_answer_timestamp.apply(lambda x: x.month).map({1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'})

    
    review_score_per_month = Olist.groupby(['review_month', 'review_day'], as_index=False).review_score.mean()
    #review_score_per_month = review_score_per_month.sort_values(by=['review_day'], ascending=True)

    st.markdown('**_Customer_ Rating** Each Month & DayofWeek')
    #st.markdown('Sales by **_Month_ _&_ _Each_ _Day_ _of_ _Week_ cool**.')

    
    df = review_score_per_month
    fig = px.line(df, x="review_month", y="review_score", color='review_day', title='Sales Each Month & Each DayofWeek')

    fig.update_layout(
        title="Ratings Each Month & DayofWeek",
        xaxis_title="Months",
        yaxis_title="Review Ratings",
        font=dict(
            family="Courier New, monospace",
            size=15,
            color="#7f7f7f"
        )
    )
    #fig.show()
    st.write(fig)



    st.markdown('**_Average_ _Review_ Ratings** across Product categories')
    # creating an aggregation
    avg_score_per_category = Olist.groupby('product_category_name', as_index=False).agg({'review_score': ['count', 'mean']})
    avg_score_per_category.columns = ['Product Category', 'Number of Reviews', 'Average Review Ratings']

    # filtering to show only categories with more than 50 reviews
    avg_score_per_category = avg_score_per_category[avg_score_per_category['Number of Reviews'] > 100]
    avg_score_per_category = avg_score_per_category.sort_values(by='Number of Reviews', ascending=False)

    
    avg_ratings = avg_score_per_category[:20]
    fig = px.bar(avg_ratings, x='Product Category', y='Number of Reviews',
                 hover_data=['Average Review Ratings'], color='Average Review Ratings',
                 height=500)
    fig.show()
    st.write(fig)
        
    
    total_rev_month = Olist.groupby(['order_purchase_year', 'order_purchase_mon', 'product_category_name'], as_index=False).payment_value.sum()
    #total_rev_month = total_rev_month.sort_values(by=['order_purchase_year'], ascending=True)
    total_rev_month.columns = ['Sales Year','Sales Month','Product Category' , 'Sales Revenue']

    st.markdown('**_Product_ _Wise_ Revenue**')
    df = total_rev_month
    fig = px.sunburst(df, path=['Sales Year', 'Product Category'], values='Sales Revenue',
                      color='Sales Revenue', hover_data=['Sales Revenue'],
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df['Sales Revenue'], weights=df['Sales Revenue']))
    #fig.show()
    st.write(fig)


    total_rev_hour = Olist[Olist['order_purchase_year'] == 2018].groupby(['order_purchase_hour', 'product_category_name'], as_index=False).payment_value.sum()
    #total_rev_month = total_rev_month.sort_values(by=['order_purchase_year'], ascending=True)
    total_rev_hour.columns = ['Sales Hour','Product Category' , 'Sales Revenue']

    st.markdown('Product Wise **_Revenue_ _by_ Hour**')
    df = total_rev_hour
    fig = px.sunburst(df, path=['Sales Hour', 'Product Category'], values='Sales Revenue',
                      color='Sales Revenue', hover_data=['Product Category'],
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df['Sales Revenue'], weights=df['Sales Revenue']))
    #fig.show()
    st.write(fig)


    total_rev_hour = Olist[Olist['order_purchase_year'] == 2018].groupby(['order_purchase_day', 'product_category_name'], as_index=False).payment_value.sum()
    #total_rev_month = total_rev_month.sort_values(by=['order_purchase_year'], ascending=True)
    total_rev_hour.columns = ['Sales DayofWeek','Product Category' , 'Sales Revenue']

    st.markdown('**_Product_ _Wise_ Revenue** by Day of Week')
    df = total_rev_hour
    fig = px.sunburst(df, path=['Sales DayofWeek', 'Product Category'], values='Sales Revenue',
                      color='Sales Revenue', hover_data=['Product Category'],
                      color_continuous_scale='RdBu',
                      color_continuous_midpoint=np.average(df['Sales Revenue'], weights=df['Sales Revenue']))
    #fig.show()
    fig.update_layout()
    st.write(fig)
    
    
    
elif choices == 'Customer Segmentation & LTV':
    st.subheader('Customer Segmentation & LTV')
    st.sidebar.success("Don't find Customers for your Product, find Products for your Customers")
    
    
    df_days_repurchase_subsegment_2018 = pd.read_csv('./data/df_days_repurchase_subsegment_2018.csv')
    
    st.write('Customer Segmentation')
    st.markdown('Average Gap between **_First_ _and_ _Last_ Purchase**')
    configure_plotly_browser_state()
    trace0 = go.Bar(
        x=df_days_repurchase_subsegment_2018["sub_segment"].values,
        y=df_days_repurchase_subsegment_2018["diff_order_purchase"].values,
        marker=dict(
            color=['rgba(36,123,160,1)', 
                   'rgba(75,147,177,1)',
                   'rgba(112,193,179,1)', 
                   'rgba(138,204,192,1)',
                   'rgba(243,255,189,1)',
                   'rgba(247,255,213,1)',
                   'rgba(255,22,84,1)']),
                    )

    data = [trace0]

    layout = go.Layout(
        title='Avg days between first and last purchase',
    )

    fig = go.Figure(data=data, layout=layout)
    #py.iplot(fig)
    st.write(fig)

    
   
    rfm_level_ag = pd.read_csv('./data/rfm_level_ag.csv')
    
    st.markdown('**_RFM_ _Customer_ Segmentation**')
    fig1 =go.Figure(go.Treemap(
        labels = rfm_level_ag['Customer Segment'],
        parents = ['Customer Segmentation', 'Customer Segmentation', 'Customer Segmentation', 'Customer Segmentation', 'Customer Segmentation', 'Customer Segmentation', 'Customer Segmentation'],   #rfm_level_ag[('Marketing Action', 'unique')].tolist(), 
        values= rfm_level_ag['Monetary.1']
    ))

    st.write(fig1)
    
    st.markdown('**_K-Means_ _based_ Clusters**')
    relative_imp = pd.read_csv('./data/rel_imp.csv')
    plt.figure(figsize=(13, 5))
    plt.title('Relative importance of attributes')
    fig2= sns.heatmap(data=relative_imp, annot=True, fmt='.2f', cmap='RdYlGn')
    plt.show()
    st.pyplot()
    st.write(fig2)
    
    st.markdown('**_Customer_ _Lifetime_ Value**')
    image = Image.open('./images/conditional_expected_average_profit.png')
    st.image(image, caption='Conditional expected average profit',
             use_column_width=True)

    image1 = Image.open('./images/frequency_recency_matrix.png')
    st.image(image1, caption='Frequency-Recency Matrix',
             use_column_width=True)


    image2 = Image.open('./images/plot_history_alive.png')
    st.image(image2, caption='History alive',
             use_column_width=True)


    image3 = Image.open('./images/probability_alive_matrix.png')
    st.image(image3, caption='Probability',
             use_column_width=True)




elif choices == 'Social Media & Geography Analysis':
    st.subheader('Social Media & Geography Analysis')
    st.sidebar.success("Social Media is a whole new world, thats where the opportunity resides. Are you Analysing it?")  
    
    
    st.write('Reviews by **_State_ _&_ City**')
    if st.checkbox('Show Reviews by State & City'):
        
        features = ['customer_zip_code_prefix', 'customer_city', 'customer_state', 'review_score']
        df = Olist[features]
        df1 = df.groupby(['customer_state', 'customer_city'])['review_score'].mean().to_frame()
        st.write(df1.head(15))
    
    
    st.markdown('Top 10 **_Twitter_ #Hashtags**')
    #hashtag.drop(columns=['Unnamed: 0'])
    st.write(hashtag.head(10))
   
    
    st.markdown('**_Real_ _Time_ Search** for Top Hashtags for a Product Keyword')
    user_input = ''
    user_input = st.text_input("Enter product keyword for search", '')
    
    if not user_input:
        pass
    else:
        
        
        CONSUMER_KEY = credentials.API_KEY
        CONSUMER_SECRET = credentials.API_SECRET_KEY
        OAUTH_TOKEN = credentials.ACCESS_TOKEN
        OAUTH_TOKEN_SECRET = credentials.ACCESS_TOKEN_SECRET


        auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                                   CONSUMER_KEY, CONSUMER_SECRET)

        twitter_api = twitter.Twitter(auth=auth)

        search_result = twitter_api.search.tweets(q=user_input, count='20')

        statuses = search_result['statuses']

        for _ in range(5):
            try:
                counter = search_result['search_metadata']['next_results']
            except KeyError as e:
                break

            kwargs = dict([kv.split('=') for kv in unquote(counter[1:]).split("&")])

            search_results = twitter_api.search.tweets(**kwargs)
            statuses += search_results['statuses']

        hashtags = [hashtag['text']
                    for status in statuses
                    for hashtag in status['entities']['hashtags']]

        #print(json.dumps(hashtags[0:10], indent=1))
        hashtag_ = {}
        hashtag_['Top 10 #Hashtags'] = hashtags[0:15]
        hashtag_df = pd.DataFrame(hashtag_)
        st.write(hashtag_df)

    
    
    st.write('**_Real_ Time** Social Media Product Analysis')
    image7 = Image.open('./images/streaming_.png')
    st.image(image7, caption='Real Time Twitter Mentions and Sentiment',
             use_column_width=True)

    st.markdown('**_Customer_ Review** Across Brazil')
    
    image8 = Image.open('./images/mapplot.png')
    st.image(image8, caption='Customer Review across Brazil',
             use_column_width=True)


    

