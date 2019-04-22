n = 8
ans = []
list1 = []


def palce_queens(q, r):
    if r == n:
        list1.append(q)
        print(q)
    else:
        for j in range(n):
            legal = True
            for i in range(r):
                if q[i] == j or q[i] == j+r-i or q[i] == j-r+i:
                    legal = False
            if legal:
                q[r] = j
                palce_queens(q, r+1)

palce_queens([0,0,0,0,0,0,0,0], 0)
print(len(list1))