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

# ans)

# In[3]:


from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    # 보드 정보를 한 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # (바이러스 번호, 시간, x, y) 삽입
            data.append((graph[i][j], 0, i, j))
            
# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())
          
# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 너비 우선 탐색(BFS) 진행
while q:
    virus, s, x, y = q.popleft()
    
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, x, y))
                
print(graph[target_x - 1][target_y - 1])


# <b> 18. 괄호 변환

# ans)

# In[4]:


# '균형잡힌 괄호 문자열'의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
# '올바른 괄호 문자열'인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 갯수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # '올바른 괄호 문자열'이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # '올바른 괄호 문자열'이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer

p = input()
print(solution(p))


# <b> 19. 연산자 끼워 넣기

# In[55]:


from itertools import permutations

n = int(input())
data = list(input().split())
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

opers = ''
while True:
    if add > 0:
        add -= 1
        opers += '+ '
    if sub > 0:
        sub -= 1
        opers += '- '
    if mul > 0:
        mul -= 1
        opers += '* '
    if div > 0:
        div -= 1
        opers += '/ '
    if add == 0 and sub == 0 and mul == 0 and div == 0:
        break
        
opers = opers.split()
candidates = list(permutations(opers, n - 1))

for candidate in candidates:
    result = 0
    temp = data[0]
    for i in range(len(candidate)):
        temp = temp + candidate[i] + data[i + 1]
        result = eval(temp)
        result = int(result)
        temp = str(result)
        
    min_value = min(result, min_value)
    max_value = max(result, max_value)
    
print(max_value)
print(min_value)


# ans)

# In[3]:


n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul,div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때 나머지 제거
            div += 1
            
# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)


# <b> 20. 감시 피하기

# In[ ]:





# <b> 21. 인구 이동

# In[ ]:





# <b> 22. 블록 이동하기

# In[ ]:




