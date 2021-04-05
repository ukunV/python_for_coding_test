#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_문자열 내 마음대로 정렬하기

# In[3]:


def solution(strings, n):
    result = sorted(sorted(strings), key = lambda x: x[n])
    return result

print(solution(['sun','bed','car'],1))
print(solution(['abce','abcd','cdx'],2))


# In[2]:


def solution(strings, n):
    result = sorted(strings, key = lambda x: (x[n], x))
    return result

print(solution(['sun','bed','car'],1))
print(solution(['abce','abcd','cdx'],2))


# ans)

# In[5]:


from operator import itemgetter

def solution(strings, n):
    return sorted(sorted(strings), key = itemgetter(n))

print(solution(['sun','bed','car'],1))
print(solution(['abce','abcd','cdx'],2))

