#!/usr/bin/env python
# coding: utf-8

# <b> 1. 왕실의 나이트

# try)

# In[2]:


location = input()

x = int(location[1])
y = ord(location[0]) - 96

path = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

count = 0

for p in path:
    nx = x + p[0]
    ny = y + p[1]
    
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    
    count += 1
    
print(count)


# ans)

# In[ ]:


# 현재 나이트의 위치 입력받기
input_data = input()
row = int(cur[1])
column = ord(cur[0]) - ord('a') + 1
steps = [[-1, -2], [1, -2], [-1, 2], [1, 2],
          [-2, 1], [-2, -1], [2, 1], [2, -1]]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = row + step[1]
    if next_row >= 1 and next_column >= 1 and next_row <= 8 and next_column <= 8:
        result += 1

print(result)


# <b> 2. 게임 개발

# try)

# In[1]:


n, m = map(int, input().split())

x, y, direction = map(int, input().split())

d = [[0] * m for _ in range(n)]
d[x][y] = 1

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and graph[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if graph[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
            
        turn_time = 0
    
print(count)


# ans)

# In[20]:


# N, M을 공백으로 구분하여 입력받기
n,m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
        
print(count)

