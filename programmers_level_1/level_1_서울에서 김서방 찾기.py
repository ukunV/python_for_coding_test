#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_서울에서 김서방 찾기

# In[ ]:


def solution(seoul):
    answer = ''
    
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer += f'김서방은 {i}에 있다'
            break
    
    return answer

