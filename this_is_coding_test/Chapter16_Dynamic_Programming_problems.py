#!/usr/bin/env python
# coding: utf-8

# <b> 31. 금광

# ans)   dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])

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

# In[ ]:





# <b> 33. 퇴사

# In[ ]:





# <b> 34. 병사 배치하기

# In[ ]:





# <b> 35. 못생긴 수

# In[ ]:





# <b> 36. 편집 거리

# In[ ]:




