#!/usr/bin/env python
# coding: utf-8

# <b> 1. 1로 만들기

# ans) a_i = min(a_i - 1, a_i / 2, a_i / 3, a_i / 5) + 1

# In[3]:


# 정수 X를 입력받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(Bottom Up)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
        
print(d[x])


# <b> 2. 개미 전사

# ans) a_i = max(a_i-1, a_i-2 + k_i)

# In[4]:


# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(Bottom Up)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])
    
# 계산된 결과 출력
print(d[n - 1])


# <b> 3. 바닥 공사

# ans) a_i = a_i-1 + a_i-2 + a_i-2 = a_i-1 + a_i-2 * 2

# In[5]:


# 정수 N을 입력받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d[0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(Bottom Up)
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796
    
# 계산된 결과 출력
print(d[n])
print(d)


# <b> 4. 효율적인 화폐 구성

# ans)
#  - a_i-k를 만드는 방법이 존재하는 경우: a_i = min(a_i, a_i-k + 1)
#  - a_i-k를 만드는 방법이 존재하지 않는 경우: a_i = 10,001

# In[7]:


# 정수 N, M을 입력받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))
    
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(Bottom Up)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)
            
# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
    
print(d)

