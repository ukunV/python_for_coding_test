#!/usr/bin/env python
# coding: utf-8

# <b> level_2_다음 큰 숫자

# In[ ]:


def solution(n):
    answer = 0
    
    nt2 = str(bin(n)[2:])
    
    if nt2.count('1') == len(nt2):
        answer = int(nt2[0] + '0' + nt2[1:], 2)
        return answer
    else:
        idx = 0
        
        for i in range(len(nt2)):
            if nt2[i] == '0' and nt2[i + 1] == '1':
                idx = i
                answer = nt2[:i] + '10'
                break
        
        cnt1 = nt2[idx + 2:].count('1')
        rlen = len(nt2[idx + 2:])
        tmp = '0' * (rlen - cnt1) + '1' * cnt1
        
        answer += tmp
        answer = int(answer, 2)
        return answer        


# ans)

# In[ ]:


def solution(n):
    cnt1 = bin(n).count('1')
    
    for bi in range(n + 1, 1000001):
        if bin(bi).count('1') == cnt1:
            answer = bi
            return answer

