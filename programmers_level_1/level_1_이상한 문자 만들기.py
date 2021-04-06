#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_이상한 문자 만들기

# In[1]:


def solution(s):
    answer = ''
    
    for word in s.split(' '):
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        
        answer += ' '
        
    return answer[:-1]

print(solution('try          hello     world    '))

