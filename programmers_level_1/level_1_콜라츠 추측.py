#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_콜라츠 추측

# In[1]:


def solution(num):
    answer = 0
    count = 0
    while 1:
        if count == 500:
            answer = -1
            break
        if num == 1:
            answer = count
            break
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = num * 3 + 1
            count += 1
    return answer

