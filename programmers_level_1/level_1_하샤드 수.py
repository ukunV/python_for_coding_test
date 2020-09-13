#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_하샤드 수

# In[ ]:


def solution(x):
    answer = True
    temp = str(x)
    sum = 0
    for i in temp:
        sum += int(i)
    if x % sum != 0:
        answer = False
    return answer

