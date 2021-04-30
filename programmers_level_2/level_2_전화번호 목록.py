#!/usr/bin/env python
# coding: utf-8

# <b> level_2_전화번호 목록

# In[ ]:


def solution(phone_book):
    answer = True
    
    min_len = 20
    for i in range(len(phone_book)):
        if len(phone_book[i]) < min_len:
            min_len = len(phone_book[i])
    
    for i in range(len(phone_book)):
        if len(phone_book[i]) > min_len:
            phone_book[i] = phone_book[i][:min_len]
    
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j]:
                answer = False
                return answer
    
    return answer


# ans)

# In[ ]:


def solution(phone_book):
    answer = True    
    
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i + 1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                answer = False
                return answer
    
    return answer


# In[ ]:


def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            answer = False
            return answer
        
    return answer


# In[ ]:


def solution(phoneBook):
    answer = True
    
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            answer = False
            return answer
    
    return answer

