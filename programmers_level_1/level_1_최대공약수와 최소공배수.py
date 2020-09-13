#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_최대공약수와 최소공배수

# In[1]:


def solution(n, m):
    answer = []
    # 최대공약수
    if n > m:
        min = m
    else:
        min = n
    for i in range(min+1,-1,-1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    
    # 최소공배수
    for i in range(n,(n*m)+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer

print(solution(3,12))

