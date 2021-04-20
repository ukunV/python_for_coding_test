#!/usr/bin/env python
# coding: utf-8

# <b> level_2_최댓값과 최솟값

# In[14]:


def solution(s):
    tmp = s.split(' ')
    
    for i in range(len(tmp)):
        tmp[i] = int(tmp[i])
        
    answer = ''
    answer += str(min(tmp)) + ' ' + str(max(tmp))
    return answer


# ans)

# In[ ]:


def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))

