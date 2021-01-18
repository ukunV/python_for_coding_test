#!/usr/bin/env python
# coding: utf-8

# <b> 실수형

# In[6]:


# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 때 0을 생략
a = -.7
print(a)

# 10억의 지수 표현 방식(e^9)
a = 1e9
print(a)

# 752.5(e^-3)
a = 75.25e1
print(a)

#3.954(e^-3)
a = 3954e-3
print(a)

a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)
    
a = 0.3 + 0.6
print(round(a,4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)


# <b> 리스트 컴프리헨션

# In[12]:


# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
 
print(array)

# 1부터 9까지의 수의 제곱값을 포함하는 리스트
array = [i * i for i in range(1,10)]

print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 3
array = [[0] * m for _ in range(n)]
array[1][1] = 5

print(array)

# N X M 크기의 2차원 리스트 초기화(잘못된 방법)
n = 3
m = 3
array = [[0] * m] * n
array[1][1] = 5

print(array)


# <b> 리스트 관련 기타 메서드
# 
# - append(): O(N)
# - sort(reverse=True/False): O(NlogN)
# - reverse(): O(N)
# - insert(삽입할 위치 인덱스, 삽입할 값): O(N)
# - count(): O(N)
# - remove(): O(N)

# In[19]:


result = eval('3 * 5 + 9')
print(result)


# In[26]:


from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

data = ['a', 'b', 'c'] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기

print(result)

data = ['a', 'b', 'c'] # 데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(result)

data = ['a', 'b', 'c'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)

print(result)

data = ['a', 'b', 'c'] # 데이터 준비
result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기(중복 허용)

print(result)


# <b> heapq

# 파이썬의 힙은 최소 힙으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.

# In[28]:


import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# 파이썬에서는 최대 힙을 제공하지 않기 때문에 heapq 라이브러리를 이용하여 최대 힙을 구현해야 할 때는 원소의 부호를 임시로 변경하는 방식을 사용한다.

# In[30]:


import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)


# <b> bisect

# - bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# - bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

# In[34]:


from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))


# bisect_left(), bisect_right() 메서드는 '정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 효과적으로 사용될 수 있다. <br> 원소의 값을 x라고 할 때, left_value <= x <= right_value인 원소의 개수를 O(logN)으로 빠르게 계산할 수 있다.

# In[37]:


from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))


# <b> collections

# - 가장 앞쪽에 원소 추가<br>
# list: O(N) // deque: O(1)
# - 가장 뒤쪽에 원소 추가<br>
# list: O(1) // deque: O(1)
# - 가장 앞쪽에 있는 원소 제거<br>
# list: O(N) // deque: O(1)
# - 가장 뒤쪽에 있는 원소 제거<br>
# list: O(1) // deque: O(1)

# In[38]:


from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))


# In[41]:


from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

