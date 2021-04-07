#!/usr/bin/env python
# coding: utf-8

# <b> level_1_소수 만들기

# In[8]:


from itertools import combinations

def is_prime(num):
    if num in (0, 1):
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def solution(nums):
    answer = 0
    
    num_list = list(combinations(nums, 3))
    sum_list = []
    
    for cand in num_list:
        sum_list.append(sum(cand))
        
    for i in sum_list:
        if is_prime(i):
            answer += 1

    return answer

