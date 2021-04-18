#!/usr/bin/env python
# coding: utf-8

# <b> level_2_예상 대진표

# ans)

# In[2]:


from collections import deque

def solution(n,a,b):
    q = [i for i in range(1,n+1)]
    print(q)
    q = deque(q)
    answer = 0

    while q:
        x = q.popleft()
        y = q.popleft()

        if [x, y] == [a, b] or [x, y] ==[b, a]: 
            answer += 1
            break

        if a in [x, y]: 
            answer += 1
            q.append(a)

        elif b in [x, y]: q.append(b)
        else: q.append(x)

    return answer

print(solution(8, 4, 7))


# In[ ]:


def solution(n,a,b):
    answer = 0
    
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer

