#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_정수 내림차순으로 배치하기

# In[5]:


def solution(n):
    tmp = sorted(str(n), reverse = True)
    answer = ''.join(tmp)
    return int(answer)

