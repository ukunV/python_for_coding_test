#!/usr/bin/env python
# coding: utf-8

# <b> level_2_이진 변환 반복하기

# In[ ]:


def solution(s):
    answer = [0, 0]
    
    while s != '1':
        cnt1 = s.count('1')
        cnt0 = s.count('0')
        
        answer[1] += cnt0
        s = bin(cnt1)[2:]
        
        answer[0] += 1
    
    return answer

