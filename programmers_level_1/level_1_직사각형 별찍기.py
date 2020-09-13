#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_직사각형 별찍기

# In[1]:


a, b = map(int, input().strip().split(' '))

for i in range(b):
    print('*' * a)

