#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_문자열 내림차순으로 배치하기

# In[8]:


def solution(s):
    answer = list(s)
    
    answer.sort(reverse = True)
    
    answer = ''.join(answer)
    
    return answer

print(solution('Zbatews'))

