#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_문자열 내 p와 y의 개수

# In[2]:


def solution(s):
    p_count = 0
    y_count = 0
    for i in s:
        if i in ('p','P'):
            p_count += 1
        elif i in ('y','Y'):
            y_count += 1
            
    if p_count == y_count:
        return True
    else:
        return False
    
print(solution('pPoooyY'))
print(solution('Pyy'))

