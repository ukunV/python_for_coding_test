#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_소수 찾기(*)

# In[1]:


def solution(n):
    answer = 0
    ns = set([i for i in range(3,n+1,2)])
    for i in range(3,n+1,2):
        if i in ns:
            ns -= set([i for i in range(i*2,n+1,i)])
            
    answer = len(ns) + 1
    return answer

print(solution(5))

