#!/usr/bin/env python
# coding: utf-8

# <b> 01. 모험가 길드

# try)

# In[ ]:


n = int(input())
data = list(map(int, input().split()))
data.sort()

cnt_group = 0
cnt_people = 0

for i in data:
    cnt_people += 1
    if cnt_people >= i:
        cnt_group += 1
        cnt_people = 0
        
print(cnt_group)


# ans)

# In[3]:


n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
        
print(result) # 총 그룹의 수 출력


# <b> 02. 곱하기 혹은 더하기

# try)

# In[ ]:


ns = input()

result = int(ns[0])
for i in range(1, len(ns)):
    if int(ns[i]) == 1 or int(ns[i]) == 0 or result == 0 or result == 1:
        result += int(ns[i])
    else:
        result *= int(ns[i])
        
print(result)


# In[2]:


n = input()

result = int(n[0])
for i in range(1, len(n)):
    if int(n[i]) in (0, 1) or result in (0, 1):
        result += int(n[i])
    else:
        result *= int(n[i])
        
print(result)


# ans)

# In[10]:


data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        
print(result)


# <b> 03. 문자열 뒤집기

# try)

# In[10]:


data = input()

all_0 = 0
all_1 = 0

for i in range(len(data) - 1):
    if data[i] == data[i+1]:
        continue
    if data[i] == '0':
        all_0 += 1
    else:
        all_1 += 1
        
print(min(all_0, all_1))


# In[6]:


data = input()

temp = data[0]

if temp == '0':
    cnt_0 = 1
    cnt_1 = 0
else:
    cnt_0 = 0
    cnt_1 = 1
    
for i in range(1, len(data)):
    if data[i] == temp:
        continue
    else:
        if data[i] == '0':
            cnt_0 += 1
            temp = '0'
        else:
            cnt_1 += 1
            temp = '1'
            
print(min(cnt_0, cnt_1))


# ans)

# In[15]:


data = input()
count_0 = 0 # 전부 0으로 바꾸는 경우
count_1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count_0 += 1
else:
    count_1 += 1
    
# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count_0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count_1 += 1
            
print(min(count_0, count_1))


# <b> 04. 만들 수 없는 금액

# try)

# ans)

# In[20]:


n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x
    
# 만들 수 없는 금액 출력
print(target)


# <b> 05. 볼링공 고르기

# try)

# In[32]:


n,m = map(int, input().split())
ws = list(map(int, input().split()))
wc = [0] * (n + 1)

for w in ws:
    wc[w] += 1
    
result = 0
temp = 0
for i in range(1, n):
    if wc[i] == 0:
        continue
    temp += wc[i]
    result += ((sum(wc) - temp) * wc[i])

print(result)


# ans)

# In[ ]:


n, m = map(int, input().split()) # n: 볼링공의 갯수, m: 가장 무거운 볼링공의 무게
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11
for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
    
result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기
    
print(result)


# <b> 06. 무지의 먹방 라이브

# try)

# ans)

# In[1]:


import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))
        
    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 K 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

food_times = [3, 1, 2]
print(solution(food_times, 5), '번')

