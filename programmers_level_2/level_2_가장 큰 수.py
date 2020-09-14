#!/usr/bin/env python
# coding: utf-8

# <b>Level 2_가장 큰 수(*)

# In[ ]:


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

