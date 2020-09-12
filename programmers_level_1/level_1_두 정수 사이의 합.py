#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_두 정수 사이의 합

# In[1]:


def solution(a, b):
    answer = 0
    if a < b:
        for i in range(a,b+1):
            answer += i
        return answer
    else:
        for i in range(b, a+1):
            answer += i
        return answer

print(solution(5,3))

