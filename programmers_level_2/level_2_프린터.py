#!/usr/bin/env python
# coding: utf-8

# <b> level_2_프린터

# In[11]:


from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque([(i, j) for i, j in enumerate(priorities)])
    
    result = []
    while q:
        if q[0][1] == max(q, key=lambda x:x[1])[1]:
            result.append(q.popleft())
        else:
            tmp = q.popleft()
            q.append(tmp)
            
    for i in range(len(result)):
        if result[i][0] == location:
            answer = i + 1
            break
            
    return answer

print(solution([2,1,3,2], 2))


# ans)

# In[18]:


from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque([(i,p) for i,p in enumerate(priorities)])
    
    while True:
        print(q)
        cur = q.popleft()
        if any(cur[1] < i[1] for i in q):
            q.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
            
print(solution([2,1,3,2], 1))

