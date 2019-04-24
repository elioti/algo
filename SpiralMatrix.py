#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: June
# @Time : 2019/4/24

"""
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

-> | <- |
0 +1
+1 0
0 -1
-1 0
"""

# def spiralOrder(matrix):
#     row = len(matrix[0])  # j
#     col = len(matrix)  # i
#     ans = []
#     def foo(i, j, state, flag):
#         if 0 <= i < col and 0 <= j < row and matrix[i][j] is not None:
#            ans.append(matrix[i][j])
#            matrix[i][j] = None
#            foo(i + state[0], j + state[1], state, 0)
#         else:
#             if flag == 0:
#                 tmp = state
#                 if state == (0, 1):
#                     state = (1, 0)
#                 elif state == (1, 0):
#                     state = (0, -1)
#                 elif state == (0, -1):
#                     state = (-1, 0)
#                 else:
#                     state = (0, 1)
#                 foo(i+state[0]-tmp[0], j+state[1]-tmp[1], state, 1)
#     foo(0,0,(0,1), 0)
# spiralOrder([])

def spiralOrder(num):
    row, col = num, num
    matrix = [[None for _ in range(num)] for _ in range(num)]
    def foo(i, j, state, flag, count):
        if 0 <= i < col and 0 <= j < row and matrix[i][j] is None:
           matrix[i][j] = count
           foo(i + state[0], j + state[1], state, 0, count+1)
        else:
            if flag == 0:
                tmp = state
                if state == (0, 1):
                    state = (1, 0)
                elif state == (1, 0):
                    state = (0, -1)
                elif state == (0, -1):
                    state = (-1, 0)
                else:
                    state = (0, 1)
                foo(i+state[0]-tmp[0], j+state[1]-tmp[1], state, 1, count)
    foo(0,0,(0,1), 0, 1)
    print(matrix)
spiralOrder(0)
