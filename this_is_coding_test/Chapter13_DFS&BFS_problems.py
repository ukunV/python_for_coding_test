#!/usr/bin/env python
# coding: utf-8

# <b> 15. 특정 거리의 도시 찾기

# ans)

# In[6]:


from collections import deque

# 도시의 갯수, 도로의 갯수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
        
# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)


# <b> 16. 연구소

# In[11]:


from itertools import combinations

n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))
    
comb = []
for a in range(len(data)):
    for b in range(len(data[a])):
        if data[a][b] == 0:
            comb.append((a,b))
            
candidates = list(combinations(comb, 3))
            
def count_zero(l, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if l[i][j] == 0:
                count += 1
    return count

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(temp, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >=0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(temp, nx, ny)
                
def solution(candidate, data, n, m):
    temp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]
    
    for i, j in candidate:
        temp[i][j] = 1
        
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                virus(temp, i, j)
                
    return count_zero(temp, n, m)
                
        
result = 0
for candidate in candidates:
    result = max(result, solution(candidate, data, n, m))
    
print(result)


# ans)

# In[10]:


n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))
    
# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >=0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)
                
# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최댓값 게산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
                
dfs(0)
print(result)


# <b> 17. 경쟁적 전염

# In[ ]:





# <b> 18. 괄호 변환

# In[ ]:





# <b> 19. 연산자 끼워 넣기

# In[ ]:





# <b> 20. 감시 피하기

# In[ ]:





# <b> 21. 인구 이동

# In[ ]:





# <b> 22. 블록 이동하기

# In[ ]:




