#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_제일 작은 수 제거하기

# In[ ]:


def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    arr.remove(min(arr))
    
    return arr

