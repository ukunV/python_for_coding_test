#!/usr/bin/env python
# coding: utf-8

# <b> 23. 국영수

# ans)

# In[2]:


n = int(input())
students = [] # 학생 정보를 담을 리스트
# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())
    
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])


# <b> 24. 안테나

# In[ ]:





# <b> 25. 실패율

# In[ ]:





# <b> 26. 카드 정렬하기

# In[ ]:




