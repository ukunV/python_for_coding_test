#!/usr/bin/env python
# coding: utf-8

# <b> 07. 럭키 스트레이트

# In[16]:


data = input()
n = len(data) // 2

left = 0
for i in range(n):
    left += int(data[i])

right = 0
for i in range(n, len(data)):
    right += int(data[i])
    
if left == right:
    print("LUCKY")
else:
    print("READY")


# ans)

# In[7]:


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


# <b> 08. 문자열 재정렬

# In[31]:


data = input()

alp = []
sum = 0
for i in data:
    if ord(i) >= 65 and ord(i) <= 90:
        alp.append(i)
    else:
        sum += int(i)
        
alp.sort()

if sum == 0:
    print(''.join(alp))
else:
    print(''.join(alp) + str(sum))


# ans)

# In[ ]:


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


# <b> 09. 문자열 압축 *

# ans)

# In[32]:


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


# <b> 10. 자물쇠와 열쇠

# In[ ]:





# <b> 11. 뱀

# In[ ]:





# <b> 12. 기둥과 보 설치

# In[ ]:





# <b> 13. 치킨 배달

# In[ ]:





# <b> 14. 외벽 점검

# In[ ]:




