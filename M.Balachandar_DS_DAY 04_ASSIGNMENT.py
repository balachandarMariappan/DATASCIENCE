#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Question 1
import pandas as pd
print (pd.__version__)


# In[7]:


# Question 2
import numpy as np
import pandas as pd
data=pd.Series(np.array(['apple','bat','cat','dog']))
print(data)


# In[47]:


# Question 3
import pandas as pd
df=pd.DataFrame({'a':'apple','b':'bat','c':'cat','d':'den'},index=[0])
df.reset_index(level=0,inplace=True)
df


# In[51]:


# Question 4
import seaborn as sns
mpg=sns.load_dataset("mpg")
mpg


# In[55]:


# Question 5
import seaborn as sns
mpg=sns.load_dataset("mpg")
df1=pd.DataFrame(mpg,columns=['origin'])
df1


# In[60]:


# Question 6


# In[ ]:




