#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_콜라츠 추측

# In[1]:


def solution(num):
    answer = 0
    
    if num == 1:
        return answer
    
    for _ in range(500):
        if num % 2 == 0:
            num /= 2
            answer += 1
            if num == 1:
                break
        else:
            num = num * 3 + 1
            answer += 1
            
    if num != 1:
        answer = -1
        
    return answer

