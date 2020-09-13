#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_짝수와 홀수

# In[ ]:


def solution(num):
    answer = ''
    if num % 2 == 0:
        answer += 'Even'
    else:
        answer += 'Odd'
    return answer

