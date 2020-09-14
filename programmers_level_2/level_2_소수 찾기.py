#!/usr/bin/env python
# coding: utf-8

# <b>Level 2_소수 찾기(*)

# In[1]:


from itertools import permutations
 
def solution(numbers):
    answer = 0
    
    num_list = []
    for i in range(1,len(numbers)+1) :
        test_list = permutations(numbers,i)       
        for j in test_list :
            num_list.append(int("".join(j)))
    
    num_list = list(set(num_list)) # 중복과 0, 1 제외
    if 0 in num_list :
        num_list.remove(0)        
    if 1 in num_list :
        num_list.remove(1)
    
    for i in num_list:
        if i % 2 == 0 and i != 2:
            num_list.remove(i)
            
    answer = len(num_list)
    for i in num_list:
        if i == 2:
            continue
        for j in range(3, i+1):
            if i % j == 0 and j != i:
                answer -= 1
                break
    
    return answer


print(solution('1232'))

