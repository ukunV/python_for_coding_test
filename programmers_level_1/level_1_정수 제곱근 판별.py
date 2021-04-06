#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_정수 제곱근 판별

# In[ ]:


import math

def solution(n):
    tmp = int(math.pow(n, 0.5))
    
    if tmp**2 == n:
        answer = (tmp + 1)**2
    else:
        answer = -1
        
    return answer

