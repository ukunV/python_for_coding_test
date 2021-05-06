#!/usr/bin/env python
# coding: utf-8

# <b> level_2_더 맵게

# ans)

# In[ ]:


import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    
    while scoville[0] < K:
        tmp = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, tmp)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return answer

