#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_체육복

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


# In[1]:


def solution(n, lost, reserve):
    answer = 0
    r_reserve = set(reserve) - set(lost)
    r_lost = set(lost) - set(reserve)
    answer += n - len(r_lost)
    
    for i in r_lost:
        if i - 1 in r_reserve:
            answer += 1
            r_reserve.remove(i - 1)
        elif i + 1 in r_reserve:
            answer += 1
            r_reserve.remove(i + 1)
    return answer

print(solution(5,[2,4],[1,3,5]))


# ans)

# In[ ]:


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

