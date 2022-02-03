#!/usr/bin/env python
# coding: utf-8

# <b>Level_1_폰켓몬

# try)

# In[ ]:


def solution(nums):
    answer = len(nums) / 2
    
    nums = set(nums)
    
    if answer > len(nums):
        answer = len(nums)
    
    return answer


# ans)

# In[ ]:


def solution(nums):
    return min(len(nums) / 2, len(set(nums)))

