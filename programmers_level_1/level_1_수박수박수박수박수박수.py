#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_수박수박수박수박수박수?

# In[ ]:


def solution(n):
    answer = ''
    answer += '수박'*(n//2)
    if n % 2 == 1:
        answer += '수'
    return answer

