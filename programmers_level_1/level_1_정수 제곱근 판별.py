#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_정수 제곱근 판별

# In[ ]:


def solution(n):
    answer = 0
    for i in range(n+1):
        if i**2 == n:
            answer = (i+1)**2
            break
        if i == n-1:
            answer = -1
    return answer

