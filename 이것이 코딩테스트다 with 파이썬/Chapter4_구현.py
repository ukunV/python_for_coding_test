#!/usr/bin/env python
# coding: utf-8

# <b> 상하좌우

# In[6]:


n = int(input())
routes = list(input().split())
x, y = 1, 1
type = ['L', 'R', 'U', 'D']

for r in routes:
    if (x==1 and r=='U') or (y==1 and r=='L'):
        continue
    if r=='L': y -= 1
    if r=='R': y += 1
    if r=='U': x -= 1
    if r=='D': x += 1
    
print(x, y)


# In[7]:


n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x,y)


# <b>시각

# In[9]:


n = int(input())
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)


# <b>왕실의 나이트

# In[18]:


cur = input()
row = int(cur[1])
col = ord(cur[0]) - ord('a') + 1
routes = [[-1, -2], [1, -2], [-1, 2], [1, 2],
          [-2, 1], [-2, -1], [2, 1], [2, -1]]

count = 0
for i, j in routes:
    tr = row + i
    tc = col + j
    if tr >= 1 and tc >= 1 and tr <= 8 and tc <= 8:
        count += 1

print(count)


# <b>게임 개발

# In[20]:


n,m = map(int, input().split())
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
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
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
        
print(count)

