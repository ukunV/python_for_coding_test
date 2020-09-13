#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_체육복(*)

# In[1]:


def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    for i in list(set_lost):
        if i - 1 in set_reserve:
            set_lost.remove(i)
            set_reserve.remove(i-1)
        elif i + 1 in set_reserve:
            set_lost.remove(i)
            set_reserve.remove(i+1)
    return n - len(set_lost)

print(solution(5,[2,4],[1,3,5]))

