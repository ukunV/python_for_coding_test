#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_자연수 뒤집어 배열로 만들기

# In[ ]:


def solution(n):
    answer = []
    temp = str(n)
    for i in range(len(temp)-1, -1,-1):
        answer.append(int(temp[i]))
    return answer

