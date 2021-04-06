#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_자연수 뒤집어 배열로 만들기

# In[ ]:


def solution(n):    
    answer = []
    
    for i in range(len(str(n)) - 1, -1, -1):
        answer.append(int(str(n)[i]))
        
    return answer

