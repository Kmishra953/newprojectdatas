#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('C://Users//seros//OneDrive//Desktop//Arrests.csv')
df


# In[3]:


df.head()


# In[4]:


sns.histplot(data=df , x = 'age', bins = 20 , kde = 'true')
plt.title('Distribution of age')
plt.show


# In[5]:


sns.barplot(data=df, x='year', y='checks', estimator=sum)
plt.title('year distribution')
plt.show()


# In[7]:


fig, ax = plt.subplots(figsize=(4,4))
sns.countplot(data=df ,x='colour')
plt.title('Countplot of age')
plt.show()


# In[8]:


fig1,ax1 = plt.subplots(figsize=(4,4))
sns.countplot(data=df,x='sex')
plt.title('count plot')
plt.show()


# In[10]:


sns.violinplot(data=df, x='sex', y='age')
plt.title('violinplot of sex and age')
plt.show()


# In[ ]:




