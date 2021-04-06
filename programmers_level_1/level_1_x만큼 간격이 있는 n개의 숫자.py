#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_x만큼 간격이 있는 n개의 숫자

# In[1]:


def solution(x, n):
    answer = []
    
    for i in range(1,n+1):
        answer.append(x*i)
        
    return answer

print(solution(2,5))


# ans)

# In[2]:


def solution(x, n):
    return [i*x for i in range(1,n+1)]
print(solution(2,5))

