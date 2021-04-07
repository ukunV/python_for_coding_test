#!/usr/bin/env python
# coding: utf-8

# <b> level_2_큰 수 만들기

# In[5]:


from itertools import combinations

def solution(number, k):
    comb = list(combinations(number, len(number) - k))

    nums = []
    for i in range(len(comb)):
        nums.append(''.join(comb[i]))
        
    answer = max(nums)
    
    return answer

print(solution('1924', 2))


# ans)

# In[13]:


def solution(number, k):
    answer = ''
    
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
        
    if k != 0:
        stack = stack[:-k]
        
    answer = ''.join(stack)
    return answer

print(solution('1924', 2))

