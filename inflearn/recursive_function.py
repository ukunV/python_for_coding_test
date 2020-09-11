#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 피보나치
# 0 1 1 2 3 5 8 13 21 ...

a = 0
b = 1
print(a)
for i in range(10):
    print(b)
    a, b = b, a+b


# In[5]:


# f(n) = f(n-1) + f(n-2)
def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))


# In[7]:


def s(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + s(l[1:])
    
s([100, 200, 300, 400])


# In[9]:


def f(n, e):
    if e == 1:
        return n
    else:
        return n * f(n, e-1)

f(2, 6)


# In[13]:


def comma(s):
    if len(s) < 3:
        return s
    else:
        return comma(s[:len(s)-3]) + '.' + s[len(s)-3:]
    
comma('10000000')


# In[17]:


n = 9999999999999999
n = format(n, ',')
print(n)

