#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_나누어 떨어지는 숫자 배열

# In[1]:


def solution(arr, divisor):
    answer = []
    non = [-1]
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    
    if len(answer) == 0:
        return non
    
    answer.sort()
    return answer

print(solution([3,2,6],10))
print(solution([5,9,7,10],5))

