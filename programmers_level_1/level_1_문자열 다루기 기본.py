#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_문자열 다루기 기본

# In[2]:


def solution(s):
    answer = True
    if len(s) not in (4,6):
        answer = False
        return answer
    for i in s:
        try:
            int(i)
        except:
            answer = False
            break
    return answer

print(solution('12'))


# In[ ]:


def solution(s):
    answer = True
    answer = s.isdigit() and (len(s) in (4,6))
    return answer

