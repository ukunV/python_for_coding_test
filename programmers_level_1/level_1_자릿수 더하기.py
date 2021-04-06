#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_자릿수 더하기

# In[ ]:


def solution(n):
    answer = 0
    
    for i in str(n):
        answer += int(i)

    return answer

