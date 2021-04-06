#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_예산

# In[1]:


def solution(d, budget):
    answer = 0
    temp = 0
    
    d.sort()
    
    for i in d:
        temp += i
        
        if temp > budget:
            break
            
        answer += 1
        
    return answer

print(solution([2,2,3,3],9))

