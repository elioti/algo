#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2019/4/23
"""
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
row = len(board)
col = len(board[0])
ans = []
word = 'ABCCED'
def search(i, j, order, past):
    if i == col or i== -1 or j == row or j == -1 or (i, j) in past:
        return
    if board[j][i] == word[order]:
        if order == len(word) -1:
            ans.append(past+[(i,j)])
        else:
            search(i+1, j, order+1, past+[(i,j)])
            search(i-1, j, order+1, past+[(i,j)])
            search(i, j+1, order+1, past+[(i,j)])
            search(i, j-1, order+1, past+[(i,j)])
for a in range(col):
    for b in range(row):
        search(a,b,0,[])
print(ans)