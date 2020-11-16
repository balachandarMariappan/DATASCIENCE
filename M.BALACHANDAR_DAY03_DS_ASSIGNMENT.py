#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question 1
import numpy as np
arr=np.arange(2,50,3)
print(arr)


# In[2]:


# Question 2
m=5
n=5
a=[]
b=[]
for i in range(m):
    x=int(input())
    a.append(x)
print(a)
for i in range(n):
    y=int(input())
    b.append(y)
print(b)
arr1=np.concatenate((a,b),axis=0)
print(arr1)
print(np.sort(arr1))


# In[9]:


# Question 3
arr2=np.array([[2,4,6,8],[1,3,5,7]])
print(arr2.ndim)# dimension
print(arr2.size)#  size of array


# In[ ]:


# Question 4


# In[12]:


# Question 5
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,0])
print(np.hstack((a,b))) # horizontally stacked
print(" ")
print(np.vstack((a,b))) # vertically stacked


# In[18]:


# Question 5
a=np.array([1,2,2,3,3,3,4,5,5,5])
unique,count=np.unique(a,return_counts=True)
print(unique) # unique elements
print(" ")
print(count) # count of elements' occurances


# In[ ]:





# In[ ]:




