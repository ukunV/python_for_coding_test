#!/usr/bin/env python
# coding: utf-8

# 문제7 - Eureka!

# In[3]:



cross = [[[3, 0, 1, 1, 8],
        [5, 0, 4, 5, 4],
        [1, 5, 0, 5, 1],
        [1, 2, 1, 0, 1],
        [0, 2, 5, 1, 1]],
       [[1, 2, 0, 3, 3],
        [1, 2, 0, 2, 4],
        [1, 2, 0, 2, 4],
        [4, 2, 0, 0, 1],
        [8, 4, 1, 1, 0]]]


# In[6]:


cross_ = cross[0] + cross[1]
cross_


# In[8]:


for i in range(4, -1, -1):
    print(i)


# In[11]:


for i in range(len(cross_)):
    for j in range(4, -1, -1):
        print(i, j, cross_[i][j])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




