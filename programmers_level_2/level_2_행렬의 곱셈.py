#!/usr/bin/env python
# coding: utf-8

# <b> level_2_행렬의 곱셈

# ans)

# In[ ]:


def solution(arr1, arr2):
    r = len(arr1)
    c = len(arr2[0])
    answer = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer


# In[ ]:


def solution(arr1, arr2):
    return [[sum(a * b for a, b in zip(arr1_row, arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]

