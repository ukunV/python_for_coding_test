#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_하샤드 수

# In[ ]:


def solution(x):
    answer = True
    tmp = str(x)
    
    sum = 0
    for i in tmp:
        sum += int(i)
        
    if x % sum == 0:
        return answer
    else:
        answer = False
        return answer

