#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_시저 암호

# In[1]:


def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
            continue
            
        r = ord(i) + n
        
        if r > 122 and 97 <= ord(i) and ord(i) <= 122:
            r -= 26
        elif r > 90 and 65 <= ord(i) and ord(i) <= 90:
            r -= 26
            
        answer += chr(r)
        
    return answer

print(solution("abcdefghijk",16))

