#!/usr/bin/env python
# coding: utf-8

# <b>Level 2_소수 찾기

# In[1]:


from itertools import permutations

def is_prime(num):
    if num in (0, 1):
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    
    nums = []
    for i in range(1, len(numbers) + 1):
        tmp = list(permutations(numbers, i))
        for j in range(len(tmp)):
            nums.append(''.join(tmp[j]))
            
    for i in range(len(nums)):
        nums[i] = int(nums[i])
        
    nums = set(nums)
    
    for num in nums:
        if is_prime(num):
            answer += 1
    
    return answer

