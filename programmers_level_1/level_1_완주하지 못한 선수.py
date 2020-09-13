#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_완주하지 못한 선수(*)

# In[ ]:


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    answer = participant[len(participant) - 1]        
    return answer

