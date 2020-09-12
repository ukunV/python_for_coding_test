#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_모의고사

# In[1]:


def solution(answers):
    answer = []
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == n1[i % 5]:
            count[0] += 1
        if answers[i] == n2[i % 8]:
            count[1] += 1
        if answers[i] == n3[i % 10]:
            count[2] += 1
            
    for i in range (len(count)):
        if count[i] == max(count):
            answer.append(i+1)

    return answer

