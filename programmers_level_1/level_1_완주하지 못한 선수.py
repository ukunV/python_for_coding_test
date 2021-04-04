#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_완주하지 못한 선수

# In[ ]:


def solution(participant, completion):
    who = ""
    for p in participant:
        if p not in completion:
            who = p
            break
        completion.remove(p)
            
    return who

print(solution(['a', 'c', 'b', 'a'], ['a', 'b', 'c']))


# ans)

# In[ ]:


import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]

print(solution(['a', 'c', 'b', 'a'], ['a', 'b', 'c']))

