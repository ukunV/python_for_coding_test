#!/usr/bin/env python
# coding: utf-8

# <b> level_2_가장 큰 정사각형 찾기

# ans)

# In[4]:


def solution(board):
    width = len(board[0])
    height = len(board)
    
    for i in range(1, height):
        for j in range(1, width):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

    return max(val for row in board for val in row) ** 2

