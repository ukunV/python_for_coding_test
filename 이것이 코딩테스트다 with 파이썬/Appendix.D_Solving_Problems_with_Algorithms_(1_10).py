#!/usr/bin/env python
# coding: utf-8

# <b> 1. 모험가 길드

# In[ ]:


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


# <b> 2. 곱하기 혹은 더하기

# In[7]:


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


# <b> 3. 문자열 뒤집기

# In[8]:


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


# <b> 4. 만들 수 없는 금액

# In[9]:


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


# <b> 5. 볼링공 고르기

# In[15]:


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


# <b> 6. 무지의 먹방 라이브

# In[19]:


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

food_times = [8, 6, 4]
print(solution(food_times, 15), '번')


# <b> 7. 럭키 스트레이트

# 항상 짝수인 수가 주어진다.
# 이 수에서 중앙값을 기준으로 왼쪽의 자릿 수 합이 오른쪽 자릿 수 합과 같으면
# LUCKY, 틀리면 READY를 print해라

# In[ ]:


n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])
    
# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])
    
# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print('LUCKY')
else:
    print('READY')


# <b> 8. 문자열 재정렬

# 알파벳 대문자와 숫자 (0~9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이 입력으로 들어오면, ABCKK13을 출력합니다.

# In[5]:


array = input()

alp = []
sum = 0

for i in array:
    if i.isdecimal():
        sum += int(i)
    else:
        alp.append(i)
    
alp.sort()

if sum == 0:
    print(''.join(alp))
else:
    print(''.join(alp) + str(sum))


# ans)

# In[ ]:


data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))


# <b> 9. 문자열 압축

# 데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다.
# 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에 서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.
# 
# 간단한 예로 "aabbaccc"의 경우 2a2ba3c(문자가 반복되지 않아 한 번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다.
# 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. 어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.
# 
# 예를 들어, "ababcdcdababcdcb"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축하다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현하는 방법이빈다.
# 
# 다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단뤼로 잘라서 압축하면 "abcabc2de"가 되지만 3개 단뤼로 자른다면 "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
# 
# 압축할 문자열 s,가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return하도록 solution함수를 완성해주세요.

# ans)

# In[9]:


def solution(s):
    answer = len(s)
    
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
                
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
        
    return compressed + ' ' + str(answer)

print(solution('ababcdcdababcdcd'))

