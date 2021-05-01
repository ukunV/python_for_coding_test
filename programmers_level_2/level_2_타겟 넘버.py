#!/usr/bin/env python
# coding: utf-8

# <b> level_2_타겟 넘버

# ans)

# In[ ]:


def solution(numbers, target):
    answer = 0
    n_len = len(numbers)
    
    def dfs(idx, result):
        if idx == n_len:
            if result == target:
                nonlocal answer
                answer += 1
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])
    
    dfs(0, 0)
    return answer


# In[ ]:


def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


# In[16]:


from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

print(solution([1,1,1,1,1], 3))

