#!/usr/bin/env python
# coding: utf-8

# <b>Level 2_124 나라의 숫자(*)

# In[1]:


def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]

print(solution(20))

