#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_행렬의 덧셈

# In[ ]:


def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        t = []
        for j in range(len(arr1[i])):
            t.append(arr1[i][j] + arr2[i][j])
        answer.append(t)  
    return answer

