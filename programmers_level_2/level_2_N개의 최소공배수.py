#!/usr/bin/env python
# coding: utf-8

# <b> level_2_N개의 최소공배수

# In[ ]:


def solution(arr):
    answer = 0
    
    mul = 1
    for i in arr:
        mul *= i
        
    for i in range(max(arr), mul + 1):
        cnt = 0
        
        for j in range(len(arr)):
            if i % arr[j] == 0:
                cnt += 1
                
        if cnt == len(arr):
            answer = i
            break
    
    return answer


# ans)

# In[ ]:


from math import gcd


def solution(arr):      
    answer = arr[0]
    
    for n in arr:
        answer = n * answer / gcd(n, answer)

    return answer

