#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_이상한 문자 만들기

# In[1]:


def solution(s):
    answer = ''
    ss = s.split(' ')
    for i in ss:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[:-1]

print(solution('try          hello     world    '))

