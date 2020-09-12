#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_문자열 내 마음대로 정렬하기(*)

# In[2]:


def sol(strings, n):
    return sorted(strings, key = lambda x : (x[n], x))

print(sol(['sun','bed','car'],1))
print(sol(['abce','abcd','cdx'],2))


# In[3]:


from operator import itemgetter

def sol(strings, n):
    return sorted(sorted(strings), key = itemgetter(n))

print(sol(['sun','bed','car'],1))
print(sol(['abce','abcd','cdx'],2))

