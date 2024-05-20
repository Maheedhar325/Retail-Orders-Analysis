#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install --upgrade pip


# In[ ]:


#install library and import
get_ipython().system('pip install kaggle')


# In[2]:


import kaggle


# In[3]:


#load the dataset

get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[4]:


#extract file from zip file

import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


# In[5]:


#Data Cleaning

import pandas as pd
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[6]:


df_backup = pd.read_csv('orders.csv', na_values = ['Not Available', 'unknown'])


# In[7]:


df.head()


# In[8]:


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(5)


# In[9]:


#Derive and Add new columns discount,sale_price and the profit after discount
df['discount'] = df['list_price']*(df['discount_percent']*0.01)
df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df


# In[51]:


#Order date object type to datetime type
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")
df


# In[10]:


df.drop(columns=['list_price','cost_price','discount_percent'],inplace = True)


# In[14]:


#load the data into sql server

import sqlalchemy as sal
engine = sal.create_engine('mssql://MAHEE_DEV/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[17]:


#load the data into sql server using append option

df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')


# In[ ]:





# In[ ]:




