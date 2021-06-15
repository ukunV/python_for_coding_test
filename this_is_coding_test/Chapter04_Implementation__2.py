#!/usr/bin/env python
# coding: utf-8

# <b> 1. 상하좌우

# try)

# In[1]:


n = int(input())
data = list(input().split())

x, y = 1, 1

for d in data:
    if (x == 1 and d == 'U') or (y == 1 and d == 'L') or(x == n and d == 'D') or (y == n and d == 'R'):
        continue
    
    if d == 'L': y -= 1
    elif d == 'R': y += 1 
    elif d == 'U': x -= 1
    else: x += 1
    
print(x, y)


# In[ ]:


n = int(input())
directions = list(input().split())

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for direction in directions:
    if direction == 'L':
        tx = x + dx[0]
        ty = y + dy[0]
        if tx > n or tx < 1 or ty > n or ty < 1:
            continue
        x, y = tx, ty
    elif direction == 'R':
        tx = x + dx[1]
        ty = y + dy[1]
        if tx > n or tx < 1 or ty > n or ty < 1:
            continue
        x, y = tx, ty
    elif direction == 'U':
        tx = x + dx[2]
        ty = y + dy[2]
        if tx > n or tx < 1 or ty > n or ty < 1:
            continue
        x, y = tx, ty
    elif direction == 'D':
        tx = x + dx[3]
        ty = y + dy[3]
        if tx > n or tx < 1 or ty > n or ty < 1:
            continue
        x, y = tx, ty
        
print(x, y)


# ans) O(N)

# In[ ]:


n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x,y)


# <b> 2. 시각

# try)

# In[ ]:


n = int(input())

count = 0

for i in range(0, n + 1):
    for j in range(0, 60):
        for k in range(0, 60):
            time = str(i) + str(j) + str(k)
            if '3' in time:
                count += 1
                
print(count)


# ans)

# In[ ]:


h = int(input())
count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)

