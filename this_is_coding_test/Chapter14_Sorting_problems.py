#!/usr/bin/env python
# coding: utf-8

# <b> 23. 국영수

# ans)

# In[2]:


n = int(input())
students = [] # 학생 정보를 담을 리스트
# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())
    
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])


# <b> 24. 안테나

# In[9]:


n = int(input())
location = list(map(int, input().split()))
location.sort()

tar = (n - 1) // 2
print(location[tar])


# ans)

# In[ ]:


n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값 (median)을 출력
print(data[(n - 1) // 2])


# <b> 25. 실패율

# In[10]:


n = int(input())
stages = list(map(int, input().split()))
stages.sort()
f_rate = []

for i in range(1, max(stages)):
    temp = stages.count(i) / len(stages)
    for j in range(len(stages)):
        if stages[0] == i:
            stages.remove(i)
        else:
            break
    f_rate.append((i, temp))

f_rate = sorted(f_rate, key=lambda t: t[1], reverse=True)

for rate in f_rate:
    print(rate[0], end= ' ')


# ans)

# In[7]:


def solution(N, stages):
    answer = []
    length = len(stages)
    
    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
            
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count
        
    # 실패율 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    #  정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer


# <b> 26. 카드 정렬하기

# In[ ]:




