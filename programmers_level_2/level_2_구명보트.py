#!/usr/bin/env python
# coding: utf-8

# <b> level_2_구명보트

# ans)

# In[ ]:


def solution(people, limit):
    answer = 0
    
    people.sort()
    
    i = 0
    j = len(people) - 1
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
            
        j -= 1
        answer += 1
        
    return answer

