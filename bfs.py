"""
97. Interleaving String
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
"""

def isInterleave(s1, s2, s3):
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 +len_s2 != len(s3):
        return False
    dict1 = {}
    def partition(i, j):
        tmp = dict1.get((i,j), None)
        if tmp is not None:
            return tmp
        if i == len_s1 and j == len_s2:
            dict1[(i, j)] = True
            return True
        else:
            a, b = False, False
            if i < len_s1 and s1[i] == s3[i+j]:
                a = partition(i+1, j)
            if j < len_s2 and s2[j] == s3[i+j]:
                b = partition(i, j+1)
            dict1[(i,j)] = a or b
            return a or b
    ans = partition(0,0)
    print(dict1)
    return ans
print(isInterleave('abbbbbbcabbacaacccababaabcccabcacbcaabbbacccaaaaaababbbacbb', 'ccaacabbacaccacababbbbabbcacccacccccaabaababacbbacabbbbabc', 'cacbabbacbbbabcbaacbbaccacaacaacccabababbbababcccbabcabbaccabcccacccaabbcbcaccccaaaaabaaaaababbbbacbbabacbbacabbbbabc'))
# print(isInterleave('aabcc','dbbca','aadbbbaccc'))