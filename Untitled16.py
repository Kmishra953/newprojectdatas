#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


train_data = pd.read_csv('C://Users//seros//OneDrive//Desktop//train.csv')
train_data


# In[3]:


train_data.head()


# In[7]:


tst_data = pd.read_csv('C://Users//seros//OneDrive//Desktop//test.csv')
tst_data.head()


# In[11]:


w = train_data.loc[train_data.Sex == 'female']['Survived']
P_women = sum(w)/len(w)
print('survived women % =',P_women)


# In[12]:


m = train_data.loc[train_data.Sex == 'male']['Survived']
P_men = sum(m)/len(m)
print('survived men % =',P_men)


# In[17]:


from sklearn.ensemble import RandomForestClassifier

y = train_data["Survived"]

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(tst_data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': tst_data.PassengerId, 'Survived': predictions})
output.to_csv('C://Users//seros//OneDrive//Desktop//submission.csv', index=False)
print("submission saved")


# In[15]:


predictions


# In[16]:


output


# In[ ]:




