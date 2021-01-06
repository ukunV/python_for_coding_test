#!/usr/bin/env python
# coding: utf-8

# <b> 소수의 판별

# In[3]:


# 소수 판별 함수
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))


# 2부터 x의 제곱근까지만 확인 -> O(X^1/2)

# In[6]:


import math

# 소수 판별 함수
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))


# <b> 에라토스테네스의 체: 매우 빠르게 동작하지만 메모리의 소비가 크다. - O(NloglogN)

# In[8]:


import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별
array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
            
# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')


# <b> 투 포인터

# 특정한 합을 가지는 부분 연속 수열 찾기: 음수 데이터가 포함되어 있는 경우 투 포인터 알고리즘 사용 불가능

# In[10]:


n = 5 # 데이터의 개수 N
m = 5 # 찾고자 하는 부분합 M
data = [1, 2, 3, 2, 5] # 전체 수열

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
    
print(count)


# 정렬되어 있는 두 리스트의 합집합(정렬)

# In[13]:


# 사전에 정렬된 리스트 A와 B선언
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

# 리스트 A와 B의 모든 원소를 담을 수 있는 크기의 결과 리스트 초기화
result = [0]* (n + m)
i = 0
j = 0
k = 0

# 모든 원소가 결과 리스트에 담길 때가지 반복
while i < n or j < m:
    # 리스트 B의 모든 원소가 처리되었거나, 리스트 A의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        # 리스트 A의 원소를 결과 리스트로 옮기기
        result[k] = a[i]
        i += 1
    # 리스트 A의 모든 원소가 처리되었거나, 리스트 B의 원소가 더 작을 때
    else:
        # 리스트 B의 원소를 결과 리스트로 옮기기
        result[k] = b[j]
        j += 1
    k += 1
    
# 결과 리스트 출력
for i in result:
    print(i, end=' ')


# <b> 구간 합 계산

# 접두사 합을 활용한 구간 합 계산 소스코드

# In[14]:


# 데이터의 개수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)
    
# 구간 합 계산(세 번째 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[4] - prefix_sum[3 - 1])


# <b> 순열과 조합

# 순열 - nPr = n! / (n - r)!

# In[20]:


import itertools

data = [1, 2, 3]

for x in itertools.permutations(data, 2):
    print(list(x))


# 조합 - nCr = n!(n-r)! / r!

# In[19]:


import itertools

data = [1, 2, 3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')


# <b> 예제 B-1) 소수구하기

# In[21]:


import math

# M과 N을 입력받기
m, n = map(int, input().split())
array = [True for i in range(1000001)] # 처음엔 모든 수가 소수(True)인 것으로 초기화
array[1] = False # 1은 소수가 아니다

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1
            
# 모든 소수 출력
for i in range(m, n + 1):
    if array[i]:
        print(i)


# <b> 예제 B-2) 암호 만들기

# In[27]:


from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u') # 5개의 모음 정의
l, c = map(int, input().split())

# 가능한 암호를 사전식으로 출력해야 하므로 입력 이후에 정렬 수행
array = input().split()
array.sort()

# 길이가 l인 모든 암호 조합을 확인
for password in combinations(array, l):
    # 패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    # 최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if count >= 1 and count <= l - 2:
        print(''.join(password))

