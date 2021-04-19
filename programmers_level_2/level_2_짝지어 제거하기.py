#!/usr/bin/env python
# coding: utf-8

# <b> level_2_짝지어 제거하기

# In[ ]:


def solution(s):
    answer = 0

    i = 0
    while True:
        if i == len(s) - 1 or len(s) in (0, 1):
            break
            
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            i = 0
        else:
            i += 1
            
    if len(s) == 0:
        answer = 1
    else:
        answer = 0
        
    print(s)
    return answer


# ans)

# In[ ]:


def solution(s): 
    stack = []
    
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
            
    answer = 0        
    
    if len(stack) == 0:
        answer = 1
        return answer
    
    else:
        return answer

