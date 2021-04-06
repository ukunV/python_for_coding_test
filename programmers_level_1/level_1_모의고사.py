#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_모의고사

# In[1]:


def solution(answers):
    answer = []
    
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    count = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == m1[(i % 5)]:
            count[0] += 1
        if answers[i] == m2[(i % 8)]:
            count[1] += 1
        if answers[i] == m3[(i % 10)]:
            count[2] += 1
            
    for num, cnt in enumerate(count):
        if cnt == max(count):
            answer.append(num + 1)
        
    return answer

