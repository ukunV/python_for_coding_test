#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_나누어 떨어지는 숫자 배열

# In[ ]:


def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if len(answer) == 0:
        return [-1]
    
    answer.sort()
    
    return answer


# ans)

# In[ ]:


def solution(arr, divisor):
    return sorted([n for n in arr if n % divisor == 0]) or [-1]

