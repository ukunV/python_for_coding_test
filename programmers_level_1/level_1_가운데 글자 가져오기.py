#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_가운데 글자 가져오기

# In[1]:


def solution(s):
    l = len(s)
    
    if l % 2 == 0:
        return s[l // 2 - 1 : l // 2 + 1]
    else:
        return s[(l // 2)]

print(solution('abcde'))
print(solution('qwer'))


# ans)

# In[2]:


def solution(str):

    return str[(len(str)-1)//2:len(str)//2+1]

print(solution('abcde'))
print(solution('qwer'))

