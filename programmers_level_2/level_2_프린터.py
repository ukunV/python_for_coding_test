#!/usr/bin/env python
# coding: utf-8

# <b>Level 2_프린터(*)

# In[1]:


def solution(priorities, location):
    answer = 0
    s = sorted(priorities, reverse = True)
    ck = 0
    while 1:
        for i, j in enumerate(priorities):
            if j == s[ck]:
                ck += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
            
        break
    return answer

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))
print(solution([9,9,1,9,9,9],2))

