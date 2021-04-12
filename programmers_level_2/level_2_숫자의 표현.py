#!/usr/bin/env python
# coding: utf-8

# <b> level_2_숫자의 표현

# In[ ]:


def solution(n):
    answer = 0
    sums = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if sums[j] >= n:
                continue
            sums[j] += i
    
    answer = sums.count(n)
    return answer


# ans)

# In[7]:


def solution(num):
    answer = 0
    
    for i in range(1, num + 1):
        s = 0
        while s < num:
            s += i
            i += 1
        if s == num:
            answer += 1

    return answer

