#!/usr/bin/env python
# coding: utf-8

# <b>위에서 아래로

# In[2]:


n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

nums.sort()
print(nums[::-1])


# ans)

# In[3]:


n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
    print(i, end = ' ')


# <b>성적이 낮은 순서로 학생 출력하기

# ans)

# In[11]:


n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append([input_data[0], int(input_data[1])])

array = sorted(arrat, key = lambda student : student[1])

for student in array:
    print(student[0], end = ' ')


# <b>두 배열의 원소 교체

# ans)

# In[4]:


n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse = True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
        
print(sum(a))

