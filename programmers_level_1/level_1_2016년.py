#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_2016년(*)

# In[1]:


import datetime as date

def ret_wd(m,d):
    ip_wd = date.datetime(2020,m,d).weekday()
    wds = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']
    return wds[ip_wd]

print(ret_wd(5,24))

