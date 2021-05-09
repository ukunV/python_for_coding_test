#!/usr/bin/env python
# coding: utf-8

# <b> level_2_오픈채팅방

# In[ ]:


def solution(record):
    answer = []
    
    r = []
    for i in range(len(record)):
        r.append(record[i].split(' '))
        
    inn = []
    for i in range(len(r)):
        if r[i][0] == 'Enter':
            for j in range(len(inn)):
                if r[i][1] == inn[j][0]:
                    inn.pop(j)
                    break
            inn.append([r[i][1], r[i][2]])
        if r[i][0] == 'Change':
            for j in range(len(inn)):
                if r[i][1] == inn[j][0]:
                    inn[j][1] = r[i][2]
                    break
                    
    for i in range(len(r)):
        if r[i][0] == 'Enter':
            for j in range(len(inn)):
                if r[i][1] == inn[j][0]:
                    answer.append(f"{inn[j][1]}님이 들어왔습니다.")
                    break
        elif r[i][0] == 'Leave':
            for j in range(len(inn)):
                if r[i][1] == inn[j][0]:
                    answer.append(f"{inn[j][1]}님이 나갔습니다.")
                    break
    
    return answer


# ans)

# In[ ]:


def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer


# In[ ]:


idDict = dict()

def solution(record):
    answer = []
    logList = []
    
    for e in record:
        dataList = e.split(" ")
        if dataList[0] == "Leave":
            logList.append([dataList[1], "님이 나갔습니다."])
        elif dataList[0] == "Enter":
            idDict[dataList[1]] = dataList[2]
            logList.append([dataList[1], "님이 들어왔습니다."])
        elif dataList[0] == "Change":
            idDict[dataList[1]] = dataList[2]

    for log in logList:
        answer.append(idDict[log[0]] + log[1])
        
    return answer

