#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_약수의 합

# In[2]:


def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0:
            answer += i
            
    return answer

print(solution(12))

