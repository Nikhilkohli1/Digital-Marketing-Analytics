
# coding: utf-8

# In[ ]:


import flask
import difflib
import pandas as pd
import os
import json 
import numpy as np
import random
import pickle
import scipy.sparse as sparse
from scipy.sparse.linalg import spsolve
from sklearn.metrics.pairwise import cosine_distances, cosine_similarity
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import csr_matrix
from datetime import datetime 


# In[ ]:


Olist_db_ = pd.read_csv('./Olist_db_ALS.csv')
Olist = pd.read_csv('./Olist_Recommendation_Dataset.csv')
Olist_details_all = pd.read_csv('./Recomm_Customer2vec.csv')
Orders_details_control = pd.read_csv('./Loyalists.csv')

X = pd.read_csv('./X_ALS.csv', index_col=0)
all_customer = list(Olist_db_.Customer_ID.unique())
Olist_customers = list(Olist.Customer_ID.unique())
Olist_bs = Olist[Olist['Customer Segment'] == 'Champions Big Spenders']
big_spenders = list(Olist_bs.Customer_ID.unique())[:30]
loyalists = list(Orders_details_control.Customer_ID.unique())
Olist_all = list(Olist_details_all.Customer_ID.unique())


# Use pickle to load in the pre-trained model.
with open('./model/SVD_ALS_model.pkl', 'rb') as f:
    SVD = pickle.load(f)
    
decomposed_matrix = SVD.fit_transform(X)
correlation_matrix = np.corrcoef(decomposed_matrix)


def Recommendations_ALS(Customer_id):
    #Olist_db_ = Olist_db_[Olist_db_.Customer_ID < 3600]
    fave_prod = Olist_db_.groupby(['Customer_ID']).max()['Product_ID'].to_frame()
    fave_prod = fave_prod.reset_index()
    Customer_id = int(Customer_id)
    
    
    #prd_id = get_prod_id(Customer_id)
    prd_id = fave_prod[fave_prod.Customer_ID == Customer_id]['Product_ID']
    #print('Cust id - ', Customer_id)
    #print(type(Customer_id))
    #print(prd_id)
    Product_id = prd_id.iloc[0]
    product_names = list(X.index)
    product_ID_Idx = product_names.index(Product_id)
    
    correlation_product_ID = correlation_matrix[product_ID_Idx]
    
    Recommend = list(X.index[correlation_product_ID > 0.70])
    # Removes the item already bought by the customer
    Recommend.remove(Product_id) 
    
    ## Getting Product names froom prediction 

    predictions = pd.DataFrame(Recommend[:20])
    predictions.columns = ['Product_ID']

    predictions['Product Name'] = predictions.Product_ID.apply(lambda x : Olist_db_[Olist_db_.Product_ID == x]['product_name'].unique()[0])
    predictions['Average Rating'] = predictions.Product_ID.apply(lambda x : Olist_db_[Olist_db_.Product_ID == x]['Ratings'].mean())
    #predictions.set_index('Product_ID')
    Recommendations = predictions[['Product Name', 'Average Rating']][:10]
    return Recommendations[:10]



### Function to get Most popular products for new user 
def get_popular_products():
    
    # converting date columns to datetime
    date_columns = ['Purchase Timestamp']
    for col in date_columns:
        Olist[col] = pd.to_datetime(Olist[col], format='%Y-%m-%d %H:%M:%S')
    Olist.columns

    currentMonth = datetime.now().month
    Olist['rating_month'] = Olist['Purchase Timestamp'].apply(lambda x: x.month)

    temp = Olist[Olist.rating_month == currentMonth]

    popular_products = pd.DataFrame(temp.groupby(['rating_month', 'product_name'], as_index=False).agg({'Review Score': ['count', 'mean']}))
    popular_products.columns = ['Rating Month','Product Name', 'Popularity', 'Average Review Ratings']
    popular_products = popular_products.sort_values('Popularity', ascending=False)
    pop = ['Product Name', 'Average Review Ratings']

    return popular_products[pop][:10]

def Upsell_products():
    Olist_Sp = Olist[Olist['Customer Segment'] == 'Champions Big Spenders']
    Olist_Spenders = Olist_Sp.groupby('product_name', as_index=False).agg({'Review Score':['mean'], 'Monetary': 'mean'})
    Olist_Spenders.columns = ['Product Name', 'Ratings', 'Price Value']
    #Olist_Spenders = Olist_Spenders[Olist_Spenders['Number of Reviews'] > 50]
    Olist_Spenders = Olist_Spenders.sort_values(['Ratings', 'Price Value'], ascending=False)
    return Olist_Spenders[:10]

    
def Recommendations_Cust2Vec(Customer_id):
    Recommendations_c2v = Olist_details_all[Olist_details_all.Customer_ID == Customer_id]
    Recommendations_c2v = Recommendations_c2v[['product_name', 'Review Score']]
    
    return Recommendations_c2v

	
	
	

app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))
            
    if flask.request.method == 'POST':
        m_name = flask.request.form['movie_name']
        c_name = int(m_name.title())
        type(c_name)
        type(m_name)
        result_final = pd.DataFrame()
        #Get Products by Popularity
        if c_name == '':
            return(flask.render_template('negative.html',name=m_name))
        
        else:
            if (c_name not in Olist_customers and c_name not in all_customer and c_name not in Olist_all):
                print('Popular products for this month')
                print('Here 1')
                result_final = get_popular_products()
            elif c_name in big_spenders:
                result_final = Upsell_products()
                print('Here 2')
            elif c_name in loyalists:
                result_final = Recommendations_Cust2Vec(c_name)
                print('Here 3')
            elif c_name in all_customer:
                result_final = Recommendations_ALS(c_name)
                print('Here 4')
            elif c_name in Olist_all:
                result_final = Recommendations_Cust2Vec(c_name)
                print('Here 5')
            #print(result_final)
            
            names = []
            ratings = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                ratings.append(str(round(result_final.iloc[i][1], 1)))

            return flask.render_template('positive.html',movie_names=names,movie_date=ratings,search_name=m_name)

if __name__ == '__main__':
    app.run()

