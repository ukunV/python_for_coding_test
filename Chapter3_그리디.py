#!/usr/bin/env python
# coding: utf-8

# <b>예제 3-1. 거스름돈

# In[2]:


n = 1260
count = 0
list = [500, 100, 50, 10]

for coin in list:
    count += n // coin
    n %= coin
    
print(count)


# <b>큰 수의 법칙

# In[19]:


n,m,k = map(int, input().split())
nums = [2,4,5,4,6]

nums.sort()
f = nums[n-1]
s = nums[n-2]

t = f*k + s
res = 0
res += (m//(k+1)) * t
res += f * (m%(k+1))
print(res)


# In[13]:


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


# In[21]:


n,m,k=map(int, input().split(' '))
data=list(map(int, input().split(' ')))

data.sort()
first=data[n-1]
second=data[n-2]

count = (m//(k+1))*k
count += m%(k+1)

result = 0
result += count * first
result += (m-count) * second
print(result)


# <b>숫자 카드 게임

# In[15]:


n,m=map(int, input().split())
card = []

for i in range(n):
    t = []
    for j in range(m):
        t.append(int(input()))
    card.append(t)

result = 0
for i in range(n):
    min_v = min(card[i])
    result = max(result, min_v)
    
print(result)    


# <b>1이 될 때까지

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


# In[29]:


n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
    
while n > 1:
    n -= 1
    result += 1
    
print(result)


# In[30]:


n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)

