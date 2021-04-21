#!/usr/bin/env python
# coding: utf-8

# <b> level_2_튜플

# In[ ]:


from collections import Counter

def solution(s):
    answer = []
    
    s = Counter(s)
    s = sorted(s.items(), key=lambda x: x[1], reverse=True)
    
    for i in s:
        if i[0].isdigit() == True:
            answer.append(int(i[0]))

    return answer


# ans)

# In[ ]:


def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


# In[ ]:


import re
from collections import Counter

def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

