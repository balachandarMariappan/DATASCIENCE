#!/usr/bin/env python
# coding: utf-8

# # PROJECT

# In[9]:


# question 1
import pandas as pd
pubg=pd.read_csv("pub.csv")
pubg


# In[13]:


# Question 2 
type(pubg.columns)


# In[16]:


# Question 3
pubg.describe()


# In[25]:


# Question 7
df=pd.DataFrame(pubg)
df.columns


# In[27]:


# Question 16
pubg.sample()


# In[ ]:




