#!/usr/bin/env python
# coding: utf-8

# <b>Level 2_가장 큰 수

# In[1]:


from itertools import permutations

def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    
    perm = list(permutations(numbers, len(numbers)))
    
    nums = []
    for i in range(len(perm)):
        nums.append(''.join(perm[i]))
        
    answer = max(nums)
    
    return answer

print(solution([111, 2, 6]))


# In[8]:


a = ['10', '2', '6']
a.sort(reverse=True)
print(a)


# ans)

# In[5]:


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

print(solution([111, 2, 6]))

