#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_자릿수 더하기

# In[ ]:


def solution(n):
    answer = 0
    temp = str(n)
    for i in temp:
        answer += int(i)
    return answer

