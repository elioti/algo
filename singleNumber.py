#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2019/4/25

"""
Single Number II
Input: [0,1,0,1,0,1,99]
Output: 99
"""
# Time Limit Exceeded
# def singleNumber(nums):
#     length = len(nums)
#     correct = (length-1)/3
#     for i in range(length):
#         print(nums[:i], nums[i+1:])
#         if len(set(nums[:i] + nums[i+1:])) == correct:
#             return nums[i]
# ans = singleNumber([99,0,1,0,1,0,1])
# print(ans)

# pass
# def singleNumber(nums):
#     dict1 = {}
#     length = len(nums)
#     for i in range(length):
#         tmp = dict1.get(nums[i], 0)
#         if tmp == 2:
#             del dict1[nums[i]]
#         else:
#             dict1[nums[i]] = tmp +1
#     print(list(dict1.keys())[0])
# ans = singleNumber([99,0,1,0,1,0,1])

# ^ & ~
# def fastSingleNumber(nums):
#     a = b = 0
#     for num in nums:
#         b = b ^ num & ~a
#         a = a ^ num & ~b
#     print(a|b)
# fastSingleNumber([1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,99,4,5,6])

"""
leetcode 136.single Number
"""

# pass
# def singleNumber(nums):
#     ans = 0
#     for i in nums:
#         ans = ans^i
#     print(ans)
# singleNumber([4,1,2,1,2])

"""
260. Single Number III
Input:  [1,2,1,3,2,5]
Output: [3,5]
"""
def singleNumber(nums):
    dict1 = {}
    ans = []
    for i in nums:
        temp = dict1.get(i, 0)
        if temp == 1:
            del dict1[i]
        else:
            dict1[i] = temp + 1
    for j in dict1:
        ans.append(j)
    print(ans)
singleNumber([1,2,1,3,2,5])

