#!/usr/bin/env python
# coding: utf-8

# <b> level_2_주식가격

# In[ ]:


def solution(prices):
    answer = []
    
    for i in range(len(prices) - 1):
        count = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                count += 1
                break
            else:
                count += 1
        answer.append(count)
    
    answer.append(0)
    return answer


# ans)

# In[ ]:


def solution(prices):
    answer = [0] * len(prices)
    
    stack = [0]
    for i in range(1, len(prices)):
        if p[i] < prices[stack[-1]]:
            for j in stack[::-1]:
                if prices[i] < prices[j]:
                    answer[j] = i-j
                    stack.remove(j)
                else:
                    break
                    
        stack.append(i)
    
    for i in range(0, len(stack) - 1):
        answer[stack[i]] = len(prices) - stack[i] - 1
    
    return answer

