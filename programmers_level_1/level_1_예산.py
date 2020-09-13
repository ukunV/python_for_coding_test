#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_예산

# In[1]:


def solution(d, budget):
    answer = 0
    d.sort()
    sum = 0
    for i in d:
        sum += i
        if sum > budget:
            break
        answer += 1
    return answer

print(solution([2,2,3,3],9))

