#!/usr/bin/env python
# coding: utf-8

# <b>Bulit-in function

# In[8]:


print(format(1000000000, ','))
print(format(1000000000, 'e'))
print(format(1000000000, 'x'))
print(format(100000, '~>020,.4f'))


# In[17]:


def f(value):
    if value % 2 == 0:
        return value
    else:
        return None
    
print(list(filter(f, range(20))))
list(map(f, range(20)))


# In[14]:


list(filter(lambda x : x % 2 == 0, range(20)))


# In[15]:


[i for i in range(20) if i % 2 ==0]


# In[18]:


list(map(lambda x : x % 2 == 0, range(20)))


# In[19]:


list(map(lambda x : x**2, range(20)))


# In[24]:


list(zip(['a','b','c','d'], [1,2,3,4], [10,20,30,40], 'ABCD'))


# In[29]:


# reversed()
# sorted()
l = [10, 5, 4, 3, 7, 6]
print(sorted(l))
print(l)
l.sort()
print(l)


# In[32]:


testCaseOne = ['abc', 'def', 'hello world', 'hello', 'python']
testCaseTwo = 'Life is too short, You need Python'.split()
testCaseThree = list(zip('anvfe', [1, 2, 5, 4, 3]))

print(sorted(testCaseOne, key=len, reverse=False))
print(sorted(testCaseTwo, key=str.lower))
print(sorted(testCaseThree, key=lambda x:x[1])) # sort by number
print(sorted(testCaseThree, key=lambda x:x[0])) # sort by alphabet


# In[33]:


5 in [1,2,3,4,5]


# In[34]:


5 not in [1,2,3,4,5]


# In[35]:


dir(l)

# 'append'
#  'clear'
#  'copy'
#  'count'
#  'extend'
#  'index'
#  'insert'
#  'pop'
#  'remove'
#  'reverse'
#  'sort'


# In[37]:


d = {'one' : 1, 'two' : 2}
del d['one']
print(d)
d['three'] = 3
print(d)


# In[38]:


dir(d)

# 'clear'
#  'copy'
#  'fromkeys'
#  'get'
#  'items'
#  'keys'
#  'pop'
#  'popitem'
#  'setdefault'
#  'update'
#  'values'


# In[39]:


s = set('11122223333344455666')
s


# In[40]:


dir(s)

# 'add'
#  'clear'
#  'copy'
#  'difference'
#  'difference_update'
#  'discard'
#  'intersection'
#  'intersection_update'
#  'isdisjoint'
#  'issubset'
#  'issuperset'
#  'pop'
#  'remove'
#  'symmetric_difference'
#  'symmetric_difference_update'
#  'union'
#  'update'


# In[43]:


s.add(7)
print(s)
s.discard(7)
print(s)
'1' in s


# In[45]:


a = {'a', 'b', 'c'}
b = {'a', 'b', 'd'}
print(a.difference(b))
print(a.intersection(b))
print(len(a.intersection(b)))
print(a.union(b))


# In[50]:


# 단톡방에 x마리의 동물이 대화를 하고 있습니다.
# 각각의 동물들이 톡을 전송할 때마다 서버에는 아래와 같이 저장됩니다.
# serverData = '개리 라이캣 개리 개리 라이캣 자바독 자바독 파이 썬'
# 1. 단톡방에는 모두 몇 마리의 동물이 있을까요? 톡은 무조건 1회 이상 전송합니다.
# 2. 단톡방에 동물들마다 몇 변의 톡을 올렸을까요?

serverData = '개리 라이캣 개리 개리 라이캣 자바독 자바독 파이 썬'

len(set(serverData.split()))

d = {}
for i in set(serverData.split()):
    print(i, serverData.split().count(i))
    d[i] = serverData.split().count(i)

print(d)


# In[52]:


'1 2 3 4 5 6 7'.split()

list(map(int, '1 2 3 4 5 6 7'.split()))

