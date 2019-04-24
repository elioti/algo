#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2019/4/23

"""
leetcode 93
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
原字符串[1,2,...,n]
假设当前分到了i, 余下[i+1, n]


"""

def restoreIpAddresses(s: str):
    total = len(s)
    tmp = []

    def partition(i, count, ans):
        if s[i:] == '' or int(s[i:]) > 255 and count == 3:
            return
        else:
            if count == 3:
                if str(int(s[i:])) == s[i:]:
                    fin = ans + [s[i:]]
                    tmp.append('.'.join(fin))
            else:
                if s[i] == '0':
                    partition(i + 1, count + 1, ans + ['0'])
                    return
                if i + 1 <= total:
                    partition(i + 1, count + 1, ans + [s[i:i + 1]])
                if i + 2 <= total:
                    partition(i + 2, count + 1, ans + [s[i:i + 2]])
                if 1 + 3 <= total and int(s[i:i + 3]) <= 255:
                    partition(i + 3, count + 1, ans + [s[i:i + 3]])

    partition(0, 0, [])
    print(tmp)
    return tmp
restoreIpAddresses('0000')
