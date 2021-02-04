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

# In[ ]:





# <b> 34. 병사 배치하기

# In[ ]:





# <b> 35. 못생긴 수

# In[ ]:





# <b> 36. 편집 거리

# In[ ]:




