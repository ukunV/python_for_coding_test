#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_최대공약수와 최소공배수

# In[ ]:


def glc(n, m):
    answer = 0
    tmp = min(n, m)
    
    for i in range(1, tmp + 1):
        if n % i == 0 and m % i == 0:
            answer = i
    
    return answer

def lcm(n, m):
    answer = 0
    tmp = n * m
    
    for i in range(tmp, max(n, m) - 1, -1):
        if i % n == 0 and i % m == 0:
            answer = i
    
    return answer
    
def solution(n, m):
    answer = []
    
    answer.append(glc(n, m))
    answer.append(lcm(n, m))
    
    return answer


# ans)

# In[2]:


def gcdlcm(a, b):
    big, small = max(a, b), min(a, b)
    tmp = 1
    
    while tmp > 0:
        tmp = big % small
        big, small = small, tmp
    answer = [big, int(a * b / big)]

    return answer

print(gcdlcm(3,12))

