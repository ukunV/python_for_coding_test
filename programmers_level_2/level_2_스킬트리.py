#!/usr/bin/env python
# coding: utf-8

# <b> level_2_스킬트리

# ans)

# * for-else: for문이 루프를 정상적으로 다 돌았다면(break되지 않았다면) else문 실행

# In[9]:


def solution(skill, skill_trees):
    answer = 0
    
    for s in skill_trees:
        skill_list = list(skill)
        
        for i in range(len(s)):
            if s[i] in skill:
                if s[i] != skill_list.pop(0):
                    break
                
        else:
            answer += 1
        
    return answer

