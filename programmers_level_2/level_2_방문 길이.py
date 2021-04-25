#!/usr/bin/env python
# coding: utf-8

# <b> level_2_방문 길이

# ans)

# In[ ]:


def solution(dirs):
    answer = 0
    
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
            
    answer = len(s) // 2
    return answer

