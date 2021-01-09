#!/usr/bin/env python
# coding: utf-8

# <b> Greedy: 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# <b> 거스름돈 -  O(K)

# ans) 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문이다.

# In[ ]:


n = 1260
count = 0
# 큰 단위의 화폐부터 차례대로 확인 (그리디)
list = [500, 100, 50, 10]

for coin in list:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

