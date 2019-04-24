# n = 8
# ans = []
# list1 = []
#
#
# def palce_queens(q, r):
#     if r == n:
#         list1.append(q)
#         print(q)
#     else:
#         for j in range(n):
#             legal = True
#             for i in range(r):
#                 if q[i] == j or q[i] == j+r-i or q[i] == j-r+i:
#                     legal = False
#             if legal:
#                 q[r] = j
#                 palce_queens(q, r+1)

# palce_queens([0,0,0,0,0,0,0,0], 0)
# print(len(list1))
# leetcode 51
# def solveNQueens(n: int):
#     ans = []
#     template = '.'*n
#     def queens(q, r):
#         if r == n:
#             ans.append([template[:i] + 'Q' + template[i+1:] for i in q])
#         else:
#             for j in range(n):
#                 legal = True
#                 for i in range(r):
#                     if q[i] == j or q[i] == j + r - i or q[i] == j - r + i:
#                         legal = False
#                 if legal:
#                     q[r] = j
#                     queens(q, r + 1)
#     queens([0 for _ in range(n)], 0)
#     return ans
#
# a = solveNQueens(n=4)
# print(a)
def solveNQueens(n: int):
    ans = []
    def queens(q, r):
        if r == n:
            ans.append(1)
        else:
            for j in range(n):
                legal = True
                for i in range(r):
                    if q[i] == j or q[i] == j + r - i or q[i] == j - r + i:
                        legal = False
                if legal:
                    q[r] = j
                    queens(q, r + 1)
    queens([0 for _ in range(n)], 0)
    return ans

a = solveNQueens(n=4)
print(a)



