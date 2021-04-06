#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_문자열 다루기 기본

# In[ ]:


def solution(s):
    answer = True
    s = list(s)
    s.sort(reverse = True)
    
    if s[0] in str(list(range(10))):
        return answer
    else:
        answer = False
        return answer


# In[19]:


def solution(s):
    answer = True
    
    if len(s) not in (4, 6):
        answer = False
        return answer
    
    for i in s:
        try:
            int(i)
        except:
            answer = False
            break
    return answer

print(solution('a1234'))
print(solution('1234'))
print(solution('a12234'))


# ans)

# In[20]:


def solution(s):
    answer = True
    answer = s.isdigit() and (len(s) in (4,6))
    return answer

print(solution('a1234'))
print(solution('1234'))
print(solution('a12234'))

