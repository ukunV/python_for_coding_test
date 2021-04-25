#!/usr/bin/env python
# coding: utf-8

# <b> level_2_위장

# In[16]:


def solution(clothes):
    answer = 1
    
    kind = dict()
    
    for i in range(len(clothes)):
        kind[clothes[i][1]] = 1
        for j in range(len(clothes)):
            if i != j and clothes[i][1] == clothes[j][1]:
                kind[clothes[i][1]] += 1
                
    values = list(kind.values())
    
    for i in range(len(values)):
        answer *= values[i] + 1
    
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))


# ans)

# In[20]:


from collections import Counter
from functools import reduce
    
def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))


# In[22]:


def solution(clothes):
    clothes_type = {}

    for c, t in clothes:
        if t not in clothes_type:
            clothes_type[t] = 1
        else:
            clothes_type[t] += 1

    cnt = 1
    for num in clothes_type.values():
        cnt *= num + 1

    return cnt - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

