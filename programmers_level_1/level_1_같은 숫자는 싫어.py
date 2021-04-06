#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_같은 숫자는 싫어

# In[1]:


def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
            
    return answer

print(solution([4, 4, 1, 1, 3, 3, 3, 5, 5]))

