#!/usr/bin/env python
# coding: utf-8

# <b>40

# In[11]:


import random

max = int(input())
num = int(input())
ws = []
for i in range(num):
    w = random.randint(10, 80)
    ws.append(w)
    print(w)
ws.sort()

res = 0
count = 0
for i in ws:
    res += i
    count += 1
    if res > max:
        res -= i
        count -= 1
        break
        
print(count)


# <b>41

# In[17]:


n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print('YES')
else:
    print('NO')


# <b>42

# In[3]:


import datetime

a = int(input())
b = int(input())
id = datetime.date(2020, a, b)
wd = ['월', '화', '수', '목', '금', '토', '일']
x = id.weekday()
print(wd[x])


# <b>43

# In[7]:


n = int(input())

def getbin(n):
    if n < 2:
        return str(n)
    else:
        return str(getbin(n // 2) + str(n % 2))

print(getbin(n))


# <b>44

# In[17]:


n = input()
res = 0

for i in n:
    res += int(i)
    
print(res)


# <b>45

# In[13]:


import time

print(dir(time))
time.localtime().tm_year


# <b>46

# In[38]:


ns = ''

for i in range(1,101):
    ns += str(i)

res = 0

for i in ns:
    res += int(i)

print(res)


# <b>47

# In[49]:


people = [
         ('이호준', '01050442903'),
         ('이호상', '01051442904'),
         ('이준호', '01050342904'),
         ('이호준', '01050442903'),
         ('이준', '01050412904'),
         ('이호', '01050443904'),
         ('이호준', '01050442903'),
         ]

print(set(people))


# <b>48

# In[62]:


s = 'AAABBBcccddd'

for i in s:
    if i.islower():
        print(i.upper(), end = '')
    else:
        print(i.lower(), end = '')


# <b>49

# In[69]:


s = '10 9 8 7 6 5 4 3 2 1'
s = s.split(' ')

for i in range(len(s)):
    s[i] = int(s[i])
max(s)


# In[74]:


s = '10 9 8 7 6 5 4 3 2 1'
data = list(map(int,s.split(' ')))
print(max(data))


# <b>50

# In[81]:


def bubble(n, data):
    for i in range(n-1):
        for j in range(n-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                
    for i in range(n):
        print(data[i], end = " ")

n = 10
data = [5,8,2,9,3,1,6,7,10,4]

bubble(n, data)


# <b>51

# In[82]:


#병합 정렬
def 병합정렬(입력리스트):
    입력리스트길이 = len(입력리스트)
    if 입력리스트길이 <= 1:
        return 입력리스트
    중간값 = 입력리스트길이 // 2
    그룹_하나 = 병합정렬(입력리스트[:중간값])
    그룹_둘 = 병합정렬(입력리스트[중간값:])
    결과값 = []

    while (그룹_하나 and 그룹_둘) :
        if (그룹_하나[0] < 그룹_둘[0]):
            결과값.append(그룹_하나.pop(0))
        else:
            결과값.append(그룹_둘.pop(0))

    while 그룹_하나:
        결과값.append(그룹_하나.pop(0))
    while 그룹_둘:
        결과값.append(그룹_둘.pop(0))
    return 결과값

주어진리스트 = [180, 145, 165, 45, 170, 175, 173, 171]
#빈칸을 채워주세요

print(병합정렬(주어진리스트))


# <b>52

# In[ ]:


def 퀵정렬(입력리스트):
    입력리스트의길이 = len(입력리스트)
    if 입력리스트의길이 <= 1:
        return 입력리스트
    기준값 = 입력리스트.pop(입력리스트의길이//2)
    그룹_하나 = []
    그룹_둘 = []
    
    for i in range(입력리스트의길이-1):
        if 입력리스트[i] < 기준값:
            그룹_하나.append(입력리스트[i])
        else:
            그룹_둘.append(입력리스트[i])
    return 퀵정렬(그룹_하나) + [기준값] + 퀵정렬(그룹_둘)

주어진리스트 = input().split(' ')
주어진리스트 = [int(i) for i in 주어진리스트]

print(퀵정렬(주어진리스트))


# <b>53

# In[8]:


def rhkfgh(s):
    count_1 = 0
    count_2 = 0
    for i in s:
        if i == '(':
            count_1 += 1
        elif i == ')':
            count_2 += 1
    if count_1 == count_2:
        print("YES")
    else:
        print("NO")

        
n = '()('
rhkfgh(n)


# In[10]:


def math(e):
    if e.count('(') == e.count(')'):
        print('YES')
    else:
        print('NO')

math('()(')


# <b>54

# In[19]:


def orm(s):
    s = s.split(' ')
    
    for i in range(len(s)-1):
        if i == (len(s) - 1):
            break
        if int(s[i]) + 1 == int(s[i + 1]):
            continue
        else:
            return False
        
    return True

s = '1 2 3 4 5'
if orm(s) == True:
    print('YES')
else:
    print('NO')


# <b>55

# In[ ]:





# <b>56

# In[38]:


nationWidth = {'korea': 220877,
               'Rusia': 17098242,
               'China': 9596961,
               'France': 543965,
               'Japan': 377915,
               'England' : 242900 }

gap = abs(nationWidth['korea'] - nationWidth['Rusia'])
sim = 'Rusia'
for i in nationWidth.values():
    temp = abs(i - nationWidth['korea'])
    if temp !=0 and temp < gap:
        sim = i
        gap = temp
        
for i,j in nationWidth.items():
    if j == sim:
        print(i)
        break


# <b>57

# In[53]:


def ccc(n):
    s = [str(i) for i in range(0,1000+1)]
    s = ''.join(s)
    return s.count('1')

print(ccc(1000))


# <b>58

# In[54]:


def com(n):
    res = format(n, ',')
    return res

print(com(123456789))


# <b>59

# In[56]:


s = input()
print('{0:=^50}'.format(s))


# <b>60

# In[59]:


student = ['강은지','김유정','박현서','최성훈','홍유진','박지호',
           '권윤일','김채리','한지호','김진이','김민호','강채연']

for number, name in enumerate(student):
    print(f'번호 : {number + 1}, 이름 : {name}')


# <b>61

# In[72]:


alp = 'abcdefghijklmnopqrstuvwxyz'
s='aaaabbbcbdd'
d = {}

for i in alp:
    d[i] = 0
for i in s:
    d[i] += 1

for i,j in d.items():
    if j != 0:
        print(f'{i}{j}', end = '')


# <b>62

# In[ ]:





# <b>63

# In[77]:


s = 'a잉 b잉 c잉 d웅'
s = s.replace(' ', '~')
print(s[0], end = '')
for i in range(len(s)):
    if s[i] == '~':
        print(s[i+1], end = '')


# In[ ]:


user_input = input().split(' ')
#print(user_input)
result = ''

for s in user_input:
    result += s[0]

print(result)


# <b>64

# In[88]:


def wjdfid(n):
    count_7 = 0
    count_3 = 0
    
    while 1:
        if n == 0:
            break
        if n >= 7:
            n -= 7
            count_7 += 1
        elif n < 7 and n >= 3:
            n -= 3
            count_3 += 1
        else:
            return -1
    
    return count_7, count_3

t = wjdfid(24)
if t != -1:
    print(f'7kg : {t[0]}EA, 3kg : {t[1]}EA')
else:
    print(t)


# <b>65

# In[100]:


a = [1,2,3,4]
b = ['a','b','c','d']
res = []
for i,j in zip(a,b):
    res.append([i,j])
print(res)


# <b>66

# In[111]:


def solution(check, rule):
    answer = []
    for block in check:
        answer.append(check_order(block, rule))
    return answer

def check_order(block, rule):
    temp = rule.index(rule[0])
    for i in block:
        if i in rule:
            if temp > rule.index(i):
                return 'impossible'
            temp = rule.index(i)
    return 'possible'

check = ["ABCDEF", "BCAD", "ADEFQRX", "BEDFG"]
rule = "ABD"    
                
print(solution(check, rule))


# <b>67

# In[120]:


def sol(n):
    sh_1 = 0
    count = 1
    for i in range(1,100):
        sh_1 += i
        count += 1
        if sh_1 > n:
            sh_2 = sh_1 - i
            break
    m = (count-1) - (sh_1 - n)
    return m, count

print(sol(59))


# <b>68

# In[127]:


def sol(l, now):
    ans = []
    now = now.split(':')
    
    for i in range(len(l)):
        t = l[i].split(':')
        

l = ["12:30", "13:20", "14:13"]
now = "12:40"

        


# In[134]:


s = "12:30"
ss = "14:13"
v = ss.split(':') - s.split(':')

