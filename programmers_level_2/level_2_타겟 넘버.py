#!/usr/bin/env python
# coding: utf-8

# <b> 타겟 넘버

# In[2]:


from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])
    count = 0
    
    while queue:
        sum, idx = queue.popleft()
        if idx == len(numbers):
            if sum == target:
                count += 1
                
        else:
            number = numbers[idx]
            queue.append((sum + number, idx + 1))
            queue.append((sum - number, idx + 1))
    return count

print(solution([1, 1, 1, 1, 1], 3))

