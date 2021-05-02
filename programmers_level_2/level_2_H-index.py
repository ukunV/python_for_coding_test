#!/usr/bin/env python
# coding: utf-8

# <b> level_2_H-index

# ans

# In[4]:


def solution(citations):
    citations.sort()
    l = len(citations)
    
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
        
    return 0

print(solution([3,0,1,6,5]))


# In[3]:


def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution([3,0,1,6,5]))


# In[14]:


a = [6,5,3,1,0]
print(list(enumerate(a, start=1)))
b = list(map(min, enumerate(a, start=1)))
print(b)

