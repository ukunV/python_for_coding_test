#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_핸드폰 번호 가리기

# In[ ]:


def solution(phone_number):
    answer = ''
    answer += '*' * (len(phone_number) - 4)
    answer += phone_number[-4:]
    return answer

