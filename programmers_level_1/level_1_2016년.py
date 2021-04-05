#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_2016년(*)

# In[1]:


import datetime

def solution(a, b):
    weekday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    return weekday[datetime.datetime(2016, a, b).weekday() + 1]

print(solution(5, 24))


# ans)

# In[4]:


def solution(a, b):
    weekday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    diff = b-1

    for i in range(a-1):
        diff += month[i]
    return weekday[diff % 7 - 2]

print(solution(5, 24))

