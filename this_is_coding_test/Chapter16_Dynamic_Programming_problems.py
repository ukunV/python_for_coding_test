#!/usr/bin/env python
# coding: utf-8

# <b> 31. 금광

# ans) dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

# In[2]:


# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for _ in range(n):
        dp.append(array[index:index + m])
        index += m
        
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
            
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    
    print(result)


# <b> 32. 정수 삼각형

# In[17]:


n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    
results = []
for i in range(len(data[n - 1])):
    result = 0
    result += data[n - 1][i]
    connect = i
    for j in range(n - 2, -1, -1):
        if connect == 0:
            result += data[j][0]
            connect = 0
        elif connect == len(data[j]):
            result += data[j][len(data[j]) - 1]
            connect = len(data[j]) - 1
        else:
            max_value = max(data[j][connect - 1], data[j][connect])
            result += max_value
            if max_value == data[i][connect - 1]:
                connect = connect - 1
            else:
                connect = connect
        
    results.append(result)
        
print(results)
print(max(results))


# ans) dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])

# In[ ]:


n = int(input())
dp = [] # 다이나믹 프로그래밍을 위한 DP 테이블 초기화

for _ in range(n):
    dp.append(list(map(int, input().split())))
    
# 다이나믹 프로그래밍으로 두 뻔째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)
        
print(max(dp[n - 1]))


# <b> 33. 퇴사

# ans) dp[i] = max(p[i] + dp[t[i] + i], max_value)

# In[1]:


n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는 데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
    
# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value
        
print(dp)
print(max_value)


# <b> 34. 병사 배치하기

# ans) 가장 긴 증가하는 부분 수열(LIS) : D[i] = max(D[i], D[j] + 1) if array[j] < array[i]

# In[ ]:


n = input()
array = list(map(int, input().split()))
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))


# <b> 35. 못생긴 수

# ans)

# In[2]:


n = int(input())

ugly = [0] * n # 못생긴 수를 담기 위한 테이블(1차원 DP  테이블)
ugly[0] = 1 # 첫 번째 못생긴 수는 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수를 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[l] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5
        
# n번째 못생긴 수를 출력
print(ugly[n - 1])
print(ugly)


# <b> 36. 편집 거리

# ans)

# - 두 문자가 같은 경우: dp[i][j] = dp[i - 1][j - 1]

# - 두 문자가 다른 경우: dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

# In[3]:


# 최소 편집 거리(Edit Distance) 계산을 위한 다이나믹 프로그래밍
def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # DP 테이블 초기 설정
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
        
    # 최소 편집 거리 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수를 그대로 대입
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else: # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중에서 최소 비용을 찾아 대입
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                
    return dp[n][m]

# 두 문자열을 입력받기
str1 = input()
str2 = input()

# 최소 편집 거리 출력
print(edit_dist(str1, str2))

