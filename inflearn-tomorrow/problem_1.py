#!/usr/bin/env python
# coding: utf-8

# <b>문제1 - 암호를 해독해라!

# In[11]:


text=['   + -- + - + -  ',
      '   + --- + - +   ',
      '   + -- + - + -  ',
      '   + - + - + - + ']
   
for i in text:
   print(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2))    


# In[17]:


# ord() : 문자 -> 숫자
# chr() : 숫자 -> 문자

l=[]
for i in text:
    l.append(chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)))    


# In[46]:


''.join(l)


# In[24]:


''.join([chr(int(i.strip().replace(' ','').replace('+','1').replace('-','0'),2)) for i in text])


# In[51]:


[i for i in range(10) if i % 2 == 0]


# In[53]:


[f'{i} X {i} = {i * j}' for i in range(2,10) for j in range(1,10)]


# In[32]:


'011011011'.replace('0','!').replace('!','+').replace('+','~')


# In[34]:


'111'.zfill(10)


# In[54]:


s = [i.strip().replace(' ','').replace('+','1').replace('-','0') for i in text]
s


# In[44]:


''.join(list(map(lambda x : chr(int(x,2)), s)))


# In[43]:


def f(x):
    return chr(int(x,2))

''.join(list(map(f, s)))
#zip

