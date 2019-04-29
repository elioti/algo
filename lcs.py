# 718. Maximum Length of Repeated Subarray
"""
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
"""


def findLength(A, B):
    len_a = len(A)
    struct = [0 for _ in range(len_a + 1)]
    ans = 0
    for b in B:
        tmp = 0
        for index, a in enumerate(A):
            tm = struct[index+1]
            if a == b:
                struct[index + 1] = tmp + 1
            else:
                # struct[index + 1] = max(struct[index + 1], struct[index])
                struct[index + 1] = 0
            tmp = tm
        m = max(struct)
        if m > ans:
            ans = m
    print(ans)

findLength([1,2,3,2,1], [3,2,1,4,7])

