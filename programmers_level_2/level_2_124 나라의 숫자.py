#!/usr/bin/env python
# coding: utf-8

# <b>Level 2_124 나라의 숫자

# ans)

# In[1]:


def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]

print(solution(20))


# In[ ]:


def solution(n):
    numbers = ['4', '1', '2']
    answer = ''
    
    while n:
        answer = numbers[n % 3] + answer
        n = n // 3 - (n % 3 == 0)
        
    return answer


# In[ ]:


def solution(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

