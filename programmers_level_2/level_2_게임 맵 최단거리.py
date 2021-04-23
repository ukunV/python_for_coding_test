#!/usr/bin/env python
# coding: utf-8

# <b> level_2_게임 맵 최단거리

# In[13]:


def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x, y = 0, 0
    
    while True:
        count = 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= m or ny >= m:
                count += 1
                continue
            if maps[nx][ny] == 0:
                count += 1
                continue
            if maps[nx][ny] < maps[x][y] and maps[nx][ny] != 1:
                count += 1
                continue
                
            maps[nx][ny] = maps[x][y] + 1
            x, y = nx, ny
            break
        
        if (maps[n - 1][m - 1] != 1) or count == 4:
            break
    
    print(maps)
    if maps[n - 1][m - 1] == 1:
        answer = -1
    else:
        answer = maps[n - 1][m - 1]
    
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))


# ans)

# In[ ]:


from collections import deque

def check(n, m, y, x, maps):
    return 0 <= y < n and 0 <= x < m and maps[y][x] == 1

def solution(maps):
    n, m = len(maps), len(maps[0])
    y, x, move = 0, 1, 2
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque([(0, 0, 1)])
    results = set((0, 0, 1))
    
    while q:
        cur = q.popleft()
        maps[cur[y]][cur[x]] = 0
        
        if cur[y] == n - 1 and cur[x] == m - 1:
            return cur[move]            
        
        for dy, dx in dirs:
            np = (cur[y] + dy, cur[x] + dx, cur[move] + 1)
            
            if check(n, m, np[y], np[x], maps) and np not in results:
                q.append(np)
                results.add(np)
        
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))


# In[49]:


from collections import deque


def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])

    graph = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append([0,0])
    
    d = [[0,1], [0,-1], [1,0], [-1,0]]
    graph[0][0] = 1

    while q:
        front = q.popleft()
        y, x = front[0], front[1]

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1 and graph[ny][nx] == 0 :
                graph[ny][nx] = graph[y][x] + 1
                q.append([ny, nx])

    if graph[n-1][m-1] == 0:
        return -1
    else:
        return graph[n-1][m-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

