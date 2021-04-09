#!/usr/bin/env python
# coding: utf-8

# <b> level_2_피보나치 수

# In[ ]:


def fibo(n, arr):
    if n == 1 or n == 2:
        return 1
    
    if arr[n] != 0:
        return arr[n]
    
    arr[n] = fibo(n - 1, arr) + fibo(n - 2, arr)
    return arr[n]

def solution(n):
    arr = [0] * (n + 1)
    
    answer = fibo(n, arr) % 1234567
    
    return answer


# ans)

# In[4]:


def solution(n):
    fibo = [0, 1]
    
    for i in range(2, n + 1):
        fibo.append((fibo[i - 2] + fibo[i - 1]) % 1234567)
        
    answer = fibo[n]
    return answer

