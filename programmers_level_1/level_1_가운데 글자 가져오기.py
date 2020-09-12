#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_가운데 글자 가져오기

# In[ ]:


def mid_w(s):
    res = ''
    if len(s) % 2 == 1:
        idx = len(s) // 2 + 1
        res += s[idx-1]
    else:
        idx = len(s) // 2
        res += s[idx-1]+s[idx]
        
    return res

print(mid_w('abcde'))
print(mid_w('qwer'))

