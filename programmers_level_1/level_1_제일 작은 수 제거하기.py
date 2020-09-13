#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_제일 작은 수 제거하기

# In[ ]:


def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
        return answer
    answer = arr
    answer.remove(min(answer))
    return answer

