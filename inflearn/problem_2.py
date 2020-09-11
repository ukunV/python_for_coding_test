#!/usr/bin/env python
# coding: utf-8

# In[9]:


돌의내구도 = [1, 2, 1, 4]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    }]


# In[4]:


def 징검다리를건너라(돌의내구도, 독):
    answer=[i['이름'] for i in 독]
    return answer

print(징검다리를건너라(돌의내구도, 독))


# In[46]:


def 징검다리를건너라(돌의내구도, 독):
    answer=[i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도)-1:
            독의위치 += int(i['점프력'])
            돌의내구도[독의위치-1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1] < 0:
                answer[answer.index(i['이름'])] = 'fail'
                break
    return [i for i in answer if i != 'fail']

print(징검다리를건너라(돌의내구도.copy(), 독.copy()))


# In[22]:


ll=[1,2,3,4,5]

def change(l):
    l[0]=1000
change(ll)
#list는 주소로 접근한다.
ll


# In[24]:


xx=100

def change(x):
    x+=1000
change(xx)
#지역변수는 값으로 접근한다.
xx


# In[26]:


#remove : O(n)
#del : O(1)

def 징검다리를건너라(돌의내구도, 독):
    answer=[i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도)-1:
            독의위치 += int(i['점프력'])
            돌의내구도[독의위치-1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1] < 0:
                del answer[answer.index(i['이름'])]
                break
    return answer

print(징검다리를건너라(돌의내구도.copy(), 독.copy()))


# In[30]:


#remove : O(n)
#del : O(1)

돌의내구도 = [5,3,4,1,3,8,3]

def 징검다리를건너라(돌의내구도, 독):
    answer=[i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도)-1:
            독의위치 += int(i['점프력'])
            돌의내구도[독의위치-1] -= int(i['몸무게'])
            if 돌의내구도[독의위치-1] < 0:
                del answer[answer.index(i['이름'])]
                break
    return answer

print(징검다리를건너라(돌의내구도.copy(), 독.copy()))


# In[44]:


import json

JSON독 = json.dumps(독, ensure_ascii=False)
#dumps : json encodeing(python -> json)
JSON독#[:10]


# In[41]:


JSON독 = json.loads(JSON독)
#loads : json decoding(json -> python)
JSON독


# In[36]:


JSON독[0]

