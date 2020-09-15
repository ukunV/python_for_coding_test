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


# In[3]:


n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse = True)

for i in array:
    print(i, end = ' ')


# <b>성적이 낮은 순서로 학생 출력하기

# In[11]:


n = int(input())

students = []
for i in range(n):
    data = input().split()
    students.append([data[0], int(data[1])])

students = sorted(students, key = lambda a : a[1])

for i, j in students:
    print(i, end = ' ')


# <b>두 배열의 원소 교체

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

