#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_정수 내림차순으로 배치하기

# In[ ]:


def solution(n):
    answer = 0
    temp = str(n)
    nl = []
    for i in temp:
        nl.append(int(i))
    nl.sort()
    for i in range(len(nl)-1,-1,-1):
        answer += nl[i] * (10**i)
    return answer

