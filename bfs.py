"""
97. Interleaving String
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
"""

def isInterleave(s1, s2, s3):
    len_s1 = len(s1)
    len_s2 = len(s2)
    ans = False
    def partition(i, j):
        global ans
        if i == len_s1 and j == len_s2:
            print('aa')
            ans = True
            print(ans)
            return
        else:
            if i < len_s1 and s1[i] == s3[i+j]:
                partition(i+1, j)
            if j < len_s2 and s2[j] == s3[i+j]:
                partition(i, j+1)
            else:
                return
    partition(0,0)
    print(ans)
isInterleave('aabcc', 'dbbca', 'aadbbcbcac')