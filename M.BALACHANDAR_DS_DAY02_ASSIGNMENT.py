#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Question 1 >> list with even numbers
a=[]
for i in range(10):
    b=int(input())
    if(b%2!=0):
        continue
    else:
        a.append(b)
print(a)
        


# ## Question 2 >> list comprehension

# In[15]:


# iterating through a string using for loop
a=[]
for i in  "letsupgrade":
    a.append(i)
print(a)


# In[16]:


# using lambda function inside the list
a=list(map(lambda x:x**2,range(10)))
print(a)


# In[17]:


# using if inside with list comprehension
a=[x for x in range(10) if(x%2==0)]
print(a)


# In[18]:


# using nested-if with list comprehension
a=[x for x in range(100) if(x%2==0) if(x%5==0)]
print(a)


# In[19]:


#using if-else with list comprehension
a=["Even" if(i%2==0) else "Odd" for i in range(10)]
print(a)


# In[20]:


# Question 3 >> Dictionary
d=dict()
n=int(input())
for i in range(1,n+1):
    d[i]=i**2
print(d)


# In[1]:


# Question 4 >> Robot movement
import math
n=int(input())
p=[0,0]
for i in range(n):
    s=input()
    t=s.split()
    d=t[0]
    s=int(t[1])
    if(d=="UP"):
        p[0]+=s
    elif(d=="DOWN"):
        p[0]-=s
    elif(d=="LEFT"):
        p[1]-=s
    elif(d=="RIGHT"):
        p[1]+=s
    else:
        pass
print(round(math.sqrt(p[0]**2+p[1]**2)))
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




