#!/usr/bin/env python
# coding: utf-8

# <b>Level 1_K번째수

# In[1]:


def solution(array, commands):
    result = []
    for i in range(len(commands)):
        temp = array[commands[i][0] - 1 : commands[i][1]]
        temp.sort()
        result.append(temp[commands[i][2] - 1])
    
    return result


array = [1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
print(solution(array,commands))


# ans)

# In[2]:


def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

array = [1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
print(solution(array,commands))

