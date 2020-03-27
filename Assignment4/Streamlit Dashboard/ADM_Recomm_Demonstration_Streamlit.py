#!/usr/bin/env python
# coding: utf-8

# In[49]:


import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from deepctr.models import xDeepFM
from deepctr.inputs import  SparseFeat, DenseFeat,get_feature_names
import pickle
import plotly.express as px
import json
import plotly.figure_factory as ff
import time

from PIL import Image

import glob
from IPython.display import display, HTML
from tqdm import tqdm_notebook as tqdm
from sklearn.manifold import TSNE

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn import preprocessing
#pd.set_option('display.max_rows', 500)
#pd.set_option('display.max_columns', 500)
#pd.set_option('display.width', 1000)
#pd.set_option('display.max_colwidth', 500)

import papermill as pm
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from reco_utils.dataset import movielens

from reco_utils.dataset.wikidata import (search_wikidata, 
                                         find_wikidata_id, 
                                         query_entity_links, 
                                         read_linked_entities,
                                         query_entity_description)



from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import matplotlib
import matplotlib.pyplot as plt
import os
import seaborn as sns
#matplotlib.use('Agg')

import warnings
warnings.filterwarnings('ignore')

#%matplotlib inline


# In[4]:


os.chdir(r'N:\ALGORITHMIC MARKETING\Assignment4\data\Customer2Vec')


# In[5]:


df_Snacks_XDeepFM = pd.read_csv('Snacks_CTR_Data.csv')
df_Snacks_XDeepFM = df_Snacks_XDeepFM.drop(columns=['Customer_Id', 'Campaign_id','Unnamed: 0'])
df_Snacks_XDeepFM.head()


# In[53]:



df_Snacks_XDeep = df_Snacks_XDeepFM[['label','Customer_Name', 'Campaign_name' ,'I5', 'I3', 'C1', 'C2', 'C3', 'C4', 'C5']]


# In[6]:


with open('train_history.txt') as f:
    train_history1 = json.load(f)

results_list = pd.read_csv('results_list.csv', index_col=[0])
tsne_doc_features = pd.read_csv('tsne_doc_features.csv', index_col=[0])
tsne_doc = pd.read_csv('tsne_doc.csv', index_col=[0])
feature_df = pd.read_csv('feature_df.csv', index_col=[0])
feature_df['latent_cluster'] = tsne_doc['cluster']
prior_orders_details_clustered = pd.read_csv('prior_orders_detail.csv', index_col=[0])


# In[11]:




st.title("Recommendation System Dashboard")

st.markdown("""
<style>
body {
    color: #fff;
    background-color: #0A3648;
}
</style>
    """, unsafe_allow_html=True)
    
#menu
menu=["Dataset Schema","xDeepFM","Customer2Vec","Customer2Vec Clusters","Knowledge Graph"]
choices = st.sidebar.selectbox("Select Recommendation Algorithm",menu)
    
if choices == 'xDeepFM':
    st.subheader('Extreme Deep Factorization')
    st.sidebar.success("xDeepFM is a deep learning based algorithm for implicit and explicit feedback with user/item features     This is a hybrid approach where it tries to learn both implicit and explicit features.     All examples of the hybrid category use Deep Neural Networks to learn     implicit bitwise feature interactions.     They differ in how the high order feature interactions are learned")
    
    image = Image.open('xdeep.PNG')
    st.image(image, caption='Extreme Deep Factorization Model',
         use_column_width=True)
    
    #chck = st.checkbox('Show Dataframe')
    if st.checkbox('Show Dataframe'):
        st.write(df_Snacks_XDeep)
      
    
    st.write('Click Label Count')
    st.write(sns.countplot(df_Snacks_XDeepFM['label'],label="Count"))
    st.pyplot()
    st.write('Feature Coorelation Heatmap')
    st.write(sns.heatmap(df_Snacks_XDeepFM.corr()))
    st.pyplot()
    
    st.write('XDeepFM Model Metrics')
    hist_data = [train_history1['binary_crossentropy'],train_history1['val_binary_crossentropy'], train_history1['loss'], train_history1['val_loss']]

    group_labels = ['Cross Entropy','val_binary_crossentropy', 'Loss', 'val_loss']
    fig = ff.create_distplot(
    hist_data, group_labels, bin_size=[.1, .1, .1, .1])
    st.plotly_chart(fig, use_container_width=True)
    
    
    # summarize history for accuracy
    st.write('XDeepFM Model Crossentropy')
    plt.plot(train_history1['binary_crossentropy'])
    plt.plot(train_history1['val_binary_crossentropy'])
    plt.title('Model Cross Entropy')
    plt.ylabel('Binary Cross Entropy')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    st.pyplot()
    # summarize history for loss
    st.write('xDeepFM Model Loss')
    plt.plot(train_history1['loss'])
    plt.plot(train_history1['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    st.pyplot()
        
elif choices == 'Customer2Vec':
    st.subheader("Customer2Vec Embedding Algorithm")
    st.sidebar.success("We learn good semantic representations for customers (users) from transactional data using doc2vec     Each customer is a document, orders are sentences, and products are words.     We also compare Customer2Vec with the baseline representations obtained using k-means on manually designed features.")
    st.write('Visualize the Basic Space Using t-SNE')  
    plt.figure(figsize=(10, 7))
    sns.scatterplot(
    x="tsne-2d-one", y="tsne-2d-two",
    data=tsne_doc_features,
    legend="full",
    alpha=0.3)
    plt.show()
    st.pyplot()
    
    st.write('Visualize the Customer Semantic Space Using t-SNE')
    plt.figure(figsize=(10,8))
    sns.scatterplot(
    x="tsne-2d-one", y="tsne-2d-two",
    data=tsne_doc,
    legend="full",
    alpha=0.3)
    plt.show()
    st.pyplot()
    
    st.write('Interactive Segmentation in the Customer Semantic Space') 
    plt.figure(figsize=(10, 8))
    
    fig = px.scatter(tsne_doc, x="tsne-2d-one", y="tsne-2d-two")
    
    #plt.show()
    st.plotly_chart(fig, use_container_width=True)
    
    
    st.write('Segmentation in the Customer Semantic Space') 
    plt.figure(figsize=(10, 8))
    sns.scatterplot(
        x="tsne-2d-one", y="tsne-2d-two",
        hue='cluster',
        palette=sns.color_palette("hls", tsne_doc['cluster'].nunique()),
        data=tsne_doc,
        legend="full",
        alpha=0.3
    )
    plt.show()
    st.pyplot()
    
    
elif choices == 'Knowledge Graph':
    st.subheader("Wikidata Knowledge Graph Extraction")
    st.sidebar.success('This is to illustrate how to extract Knowledge Graph.     Many recommendation algorithms (DKN, RippleNet, KGCN) use Knowledge Graphs (KGs) as an external source of information')
    
    G = nx.from_pandas_edgelist(results_list, 'original_entity', 'linked_entities')

    target_names = results_list[["linked_entities", "name_linked_entities"]].drop_duplicates().rename(columns={"linked_entities": "labels", "name_linked_entities": "name"})
    source_names = results_list[["original_entity", "name"]].drop_duplicates().rename(columns={"original_entity": "labels"})
    names = pd.concat([target_names, source_names])
    names = names.set_index("labels")
    names = names.to_dict()["name"]

    plt.figure(figsize=(12, 20)) 
    pos = nx.spring_layout(G)
    nx.draw(G,pos, node_size=50,font_size=8, width = 0.2)
    nx.draw_networkx_labels(G, pos, names, font_size=8)
    plt.show()
    st.pyplot()


elif choices == 'Customer2Vec Clusters':
    st.subheader("Customer2Vec Clusters")
    st.sidebar.success('We found few latent clusters using Customer2vec algorithm. These clusters can be     utilized to group similar customers in a campaign or can be recommended similar subscription of snacks or products.    This will also help in creating new combinations of products to be offered as subscription by reviewing what snacks     customers usually buy together.')
    cluster_id = 0
    clust = st.sidebar.radio(
    "Choose clusters you want to see",
    ('First', 'Second', 'Third', 'Forth', 'Seventh'))
    
    if clust == 'First':
        cluster_id = 1
        st.write('You selected First Cluster')
    elif clust == 'Second':
        cluster_id = 2
        st.write("You selected Second Cluster")
    elif clust == 'Third':
        cluster_id = 3
        st.write("You selected Third Cluster")
    elif clust == 'Forth':
        cluster_id = 4
        st.write("You selected First Cluster")
    elif clust == 'Seventh':
        cluster_id = 7
        st.write("You selected Seventh Cluster")
    
    user_input = ''
    input_lis = []
    user_lis = []
    tick = st.sidebar.checkbox('Search by User ID')
    if tick:
        st.write('Enter UserID(Sep by ,) in search box')
        user_input = st.text_input("Enter user id for search", '')
        
        

    if not user_input:

        #cluster_id = 4.0  #Tune with slider range
        prior_orders_d = prior_orders_details_clustered[prior_orders_details_clustered['latent_cluster']==cluster_id][['user_id', 'product_name']].groupby("user_id").apply(lambda order: ' > '.join(order['product_name'])).reset_index()
        st.dataframe(prior_orders_d, 3500, 700)
        #st.write(df_Snacks_XDeepFM.head())
        st.subheader("Cluster for all Products")

        snacks = ['Snakku', 'Love with food', 'Candy Club', 'Nature Box', 'ZenPop', 'World Sampler', 'FitSnack', 'Vegan Cuts',
                    'MunchPak', 'KetoKrate']
        st.subheader("Cluster for only Snacks")
        prior_orders_details_snacks = prior_orders_details_clustered[prior_orders_details_clustered.product_name.isin(snacks)] 
        #cluster_i  #Tune with slider range
        prior_orders_d_snacks = prior_orders_details_snacks[prior_orders_details_snacks['latent_cluster']==cluster_id][['user_id', 'product_name']].groupby("user_id").apply(lambda order: ' > '.join(order['product_name'])).reset_index()
        st.dataframe(prior_orders_d_snacks.style.highlight_max(axis=0), 3500, 700)
        #st.write(df_Snacks_XDeepFM.head(10))
    else: 
        input_lis = user_input.split(',')
        for u in input_lis:
            user_lis.append(int(u))
        
        prior_orders_d = prior_orders_details_clustered[prior_orders_details_clustered['latent_cluster']==cluster_id][['user_id', 'product_name']].groupby("user_id").apply(lambda order: ' > '.join(order['product_name'])).reset_index()
        st.dataframe(prior_orders_d[prior_orders_d.user_id.isin(user_lis)], 3500, 700)
        #st.write(df_Snacks_XDeepFM.head())

        snacks = ['Snakku', 'Love with food', 'Candy Club', 'Nature Box', 'ZenPop', 'World Sampler', 'FitSnack', 'Vegan Cuts',
                    'MunchPak', 'KetoKrate']
        st.subheader("Cluster for only Snacks")
        prior_orders_details_snacks = prior_orders_details_clustered[prior_orders_details_clustered.product_name.isin(snacks)] 
        #cluster_i  #Tune with slider range
        prior_orders_d_snacks = prior_orders_details_snacks[prior_orders_details_snacks['latent_cluster']==cluster_id][['user_id', 'product_name']].groupby("user_id").apply(lambda order: ' > '.join(order['product_name'])).reset_index()
        st.dataframe(prior_orders_d_snacks[prior_orders_d_snacks.user_id.isin(user_lis)], 3500, 700)
        #st.write(df_Snacks_XDeepFM.head(10))
        
elif choices == 'Experiment':
    st.subheader("Experiment")
    
    #epochs = np.arange(1,11)
       
    
elif choices == 'Dataset Schema':
    st.subheader("Dataset Schema for the two Algorithms")

    st.write('This data is based on Instacart market basket data. It has information like product details, departments etc. Later we create the list of user journey in terms of orders made by a user in chronological order. This will help us in recommending products to customer    which they are most likely to add to their cart or just continue their subscription for a particular snack category.')
    image = Image.open('customer2vec.PNG')
    st.image(image, caption='Customer2Vec Dataset Schema',
         use_column_width=True)
    
    st.write('This dataset is based on Cretio Click through rate dataset. We have columns like Customer name, Campaign details with categorical features related to the ad shown to users, user details and whether they clicked an Advertisement for a product or not.     This will be help us in recommending Products/Campaigns/Ads to customers that they are more likely to click and convert.')
    
    image = Image.open('ctr.PNG')
    st.image(image, caption='xDeepFM Dataset Schema',
         use_column_width=True)

