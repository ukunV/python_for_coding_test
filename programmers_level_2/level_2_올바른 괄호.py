#!/usr/bin/env python
# coding: utf-8

# <b> level_2_올바른 괄호

# In[ ]:


def solution(s):
    answer = True
    
    if s[0] == ")" or s[-1:] == "(" or len(s) == 1:
        answer = False
        return answer

    chk = 0
    
    for i in range(len(s)):
        if s[i] == '(':
            chk += 1
        else:
            chk -= 1
        
        if chk < 0:
            answer = False
            break
        
    if chk == 0:
        return answer
    else:
        answer = False
        return answer


# ans)

# In[ ]:


def solution(s):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif stack:
            stack.pop()
        else:
            return False
    return not stack

