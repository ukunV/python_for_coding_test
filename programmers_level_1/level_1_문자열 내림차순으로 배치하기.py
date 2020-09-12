#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_문자열 내림차순으로 배치하기

# In[1]:


def solution(s):
    answer = ''
    ans = list(s)
    ans.sort()
    for i in range(len(s)-1,-1,-1):
        answer += ans[i]
    return answer

print(solution('Zbatews'))

