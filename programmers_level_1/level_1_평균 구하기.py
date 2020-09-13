#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_평균 구하기

# In[ ]:


def solution(arr):
    answer = 0
    sum = 0
    for i in arr:
        sum += i
    answer = sum / len(arr)
    return answer

