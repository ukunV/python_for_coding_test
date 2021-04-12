#!/usr/bin/env python
# coding: utf-8

# <b> level_2_최솟값 만들기

# In[ ]:


def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]
    
    return answer


# ans)

# In[ ]:


def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))

