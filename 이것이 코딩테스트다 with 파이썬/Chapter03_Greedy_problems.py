#!/usr/bin/env python
# coding: utf-8

# <b> 1. 큰 수의 법칙

# In[2]:


n,m,k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
f = nums[n-1]
s = nums[n-2]

t = f*k + s
res = 0
res += (m//(k+1)) * t
res += f * (m%(k+1))
print(res)


# ans)

# In[4]:


n,m,k=map(int, input().split())
data=list(map(int, input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)


# 반복되는 수열 활용

# In[3]:


# N, M, K를 공백으로 구분하여 입력받기
n,m,k=map(int, input().split(' '))
# N개의 수를 공백으로 구분하여 입력받기
data=list(map(int, input().split(' ')))

data.sort() # 입력받은 수 정렬
first=data[n-1] # 가장 큰 수
second=data[n-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = (m//(k+1))*k
count += m%(k+1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기

print(result)


# <b> 2. 숫자 카드 게임

# ans)

# min() 함수 활용

# In[3]:


n,m=map(int, input().split())
card = []

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)


# 반복문 활용

# In[2]:


# N, M를 공백으로 구분하여 입력받기
n,m=map(int, input().split())
result = 0

# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)


# <b> 3. 1이 될 때까지

# In[27]:


n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k == 0:
        n /= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)


# ans)

# In[4]:


n, k = map(int, input().split())
result = 0

# N이 K이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1
    
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1
    
print(result)


# In[30]:


n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

