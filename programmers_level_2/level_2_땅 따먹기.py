#!/usr/bin/env python
# coding: utf-8

# <b> level_2_땅 따먹기

# In[ ]:


def solution(land):
    answer = max(land[0])

    idx = land[0].index(answer)
    
    for i in range(1, len(land)):
        answer += max(land[i][:idx] + land[i][idx+1:])
        idx = land[i].index(max(land[i][:idx] + land[i][idx+1:]))
        
    return answer


# ans)

# In[ ]:


def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])

