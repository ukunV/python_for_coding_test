#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_K번째수

# In[1]:


def index_k(array, commands):
    res = []
    for cmd in commands:
        temp = array[cmd[0]-1:cmd[1]]
        temp.sort()
        res.append(temp[cmd[2]-1])

    return res


array = [1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
print(index_k(array,commands))

