#!/usr/bin/env python
# coding: utf-8

# # Summary#1

# In[13]:


s = 'I love you'
print(s)
# print(dir(s))
print(s[::2])
print(s[::-1])
# l[start:stop:step]
print(s.upper())
print(s.lower())
print(s.count('o'))
ss = '        a         '
print(ss)
print(ss.strip())
a = s.split(' ')
print(a)
print("~".join(a))
print("My name is {}, I'm {} years old" .format('lee', 10))


# In[17]:


a = 2020
b = 7
c = 1
print(a,b,c, sep = '/', end = ' ')
print(a,b,c)


# In[20]:


a = 10
b = '10'
print(a + int(b))
print(str(a) + b)


# In[22]:


a = True
b = False
print(type(a))
# print(dir(a))


# In[23]:


print(bool(' '))
print(bool(''))
print(bool(0))
print(bool(1))
print(bool(2))
print(bool(-1))
print(bool(None))


# # Summary#2

# In[38]:


l = [100,200,300,400]
print(l.index(300))
l.extend([100,100,100,100])
print(l)
l.insert(3, 1000)
print(l)
l.pop()
print(l)
l.pop(2)
print(l)
print(l.count(100))
l.remove(100)
print(l)
l.reverse()
print(l)
l.sort()
print(l)
# sorted() -> return값에서만 정렬
# reversed() -> return값에서만 뒤집음


# In[40]:


l = [1,2]
t = (l, 3, 4)
print(t)
l[0] = 10
print(t)


# In[45]:


# Set
s = {100,100,200,300,300,300}
print(s)
print(type(s))
print(dir(s))

s.add(400)
print(s)
print(set('aababbbbcccccddddd'))
ss=[1,2,3]
print(s.union(ss))


# In[49]:


# Dictionary
d = {'one' : 10, 'two' : 20}
print(d.values())
print(d.keys())
print(d.items())
l = list(d.items())
print(l[0])
print(l[0][1])


# In[51]:


jeju = {'banana' : 1000, 'orange' : 2000}
seoul = jeju
jeju['orange'] = 10000
print(seoul)
print(jeju)
incheon = seoul.copy()
seoul['orange'] = 1
print(seoul)
print(incheon)


# # Summary#3

# In[65]:


l = [1, 2, 3, 4]
for i in l:
    print(i)
print('--------------------------------------')
s = {1, 2, 3, 4, 1, 1, 1}
for j in s:
    print(j)
print('--------------------------------------')
d = {'one' : 1, "two" : 2}
for k in d:
    print(k)


# In[68]:


l = [i for i in range(10)]
print(l)
ll = ['{} X {} = {}' .format(i,j,i*j) for i in range(2, 10) for j in range(1, 10)]
print(ll)


# In[71]:


l = [(1,10),(2,20),(3,30),(4,40),(5,50)]
print(l[2][1])
for i,j in l:
    print(i, j)


# In[72]:


for i, j in enumerate(range(100,1000,100), 1): # 순위 or numbering
    print(i, j)


# # Summary#4

# In[76]:


class Car():
    maxSpeed = 300
    maxPeople = 5
    def start(self):
        print('start')
    def stop(self):
        print('stop')
    def __str__(self):
        return 'hello'
    def __init__(self):
        print('create instance')
        
class Hybrid(Car): # 상속
    battery = 1000
    batteryKM = 300
    
k5 = Car()    
k3 = Hybrid()
print(k3.maxSpeed)
print(k3)


# # Summary#5

# In[79]:


age = 10
name = 'lee'
print("My name is {}. I'm {} years old" .format(name, age))
print(f"My name is {name}. I'm {age} years old")


# In[80]:


for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')


# In[84]:


import datetime

date = datetime.datetime.now()
f'{date:%Y-%m-%d-%A}'


# In[88]:


print(f'{"hello":!<10}')
print(f'{"hello":~>10}')
print(f'{"hello":=^10}')


# In[89]:


print(f'{0.456789:0.2f}')

