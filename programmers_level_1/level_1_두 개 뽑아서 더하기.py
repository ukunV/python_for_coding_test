#!/usr/bin/env python
# coding: utf-8

# <b> 두개 뽑아서 더하기

# In[2]:


def solution(numbers):
    temp = set()
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            temp.add(numbers[i] + numbers[j])
            
    result = list(temp)
    result.sort()
        
    return result

print(solution([2, 1, 3, 4, 1]))


# ans)

# In[3]:


from itertools import combinations

def solution(numbers):
    answer = set()
    for i in list(combinations(numbers, 2)):
        answer.add(sum(i))
    return sorted(answer)

print(solution([2, 1, 3, 4, 1]))

