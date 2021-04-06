#!/usr/bin/env python
# coding: utf-8

# <b> level_1_직사각형 별 찍기

# In[2]:


a, b = map(int, input().split())

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()

