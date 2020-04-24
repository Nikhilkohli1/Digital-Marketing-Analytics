#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


from PIL import Image


# In[3]:


import glob
from IPython.display import display, HTML
from tqdm import tqdm_notebook as tqdm
from sklearn import preprocessing
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)
#pd.set_option('display.max_colwidth', 500)

#import papermill as pm
import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import matplotlib
import matplotlib.pyplot as plt
import os
import seaborn as sns
#matplotlib.use('Agg')

import warnings
warnings.filterwarnings('ignore')


# In[5]:


os.chdir(r'N:\Digital Marketing Analytics\Olist DIgital Marketing Analytics\STreamlit')

# In[6]:


df= pd.read_csv('Olist_Master.csv')
df.head()


# In[8]:


df_new = df[['order_id','product_id', 'seller_id' ,'price', 'payment_type', 'customer_city', 'customer_state']]


# In[9]:


st.title("Customer Lifetime Value Dashboard")


# In[10]:


st.markdown("""
<style>
body {
    color: #fff;
    background-color: #0A3648;
}
</style>
    """, unsafe_allow_html=True)


# In[11]:


menu=["CLTV Images"]
choices = st.sidebar.selectbox("CUstomer Lifetime Value",menu)


# In[12]:


if choices == 'CLTV Images':
    st.subheader('CLTV Images')
    #st.sidebar.success("xDeepFM is a deep learning based algorithm for implicit and explicit feedback with user/item features     This is a hybrid approach where it tries to learn both implicit and explicit features.     All examples of the hybrid category use Deep Neural Networks to learn     implicit bitwise feature interactions.     They differ in how the high order feature interactions are learned")


# In[24]:


image = Image.open('CLTV-Images\conditional_expected_average_profit.png')
st.image(image, caption='Conditional expected average profit',
         use_column_width=True)


# In[26]:


image1 = Image.open('CLTV-Images\\frequency_recency_matrix.png')
st.image(image1, caption='Frequency-Recency Matrix',
         use_column_width=True)


# In[27]:


image2 = Image.open('CLTV-Images\\plot_history_alive.png')
st.image(image2, caption='History alive',
         use_column_width=True)


# In[28]:


image3 = Image.open('CLTV-Images\\probability_alive_matrix.png')
st.image(image3, caption='Probability',
         use_column_width=True)


# In[29]:


if st.checkbox('Show Dataframe'):
        st.write(df_new)
      


# In[32]:


st.write('Click Label Count')
st.write(sns.countplot(df_new['order_id'],label="Count"))
st.pyplot()
st.write('Feature Coorelation Heatmap')
st.write(sns.heatmap(df_new.corr()))
st.pyplot()

