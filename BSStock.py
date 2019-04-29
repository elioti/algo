#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2019/4/24
"""
leetcode 121 Best Time to Buy and Sell Stock
Input: [7,1,5,3,6,4]
Output: 5
"""

# Brute Force Time Limit Exceeded
# def maxProfit(prices):
#     max = 0, 0, 0
#     min = prices[0]
#     for index, i in enumerate(prices):
#         if i < min or index==0:
#             min = i
#             for j in prices[index+1:]:
#                 if j-i>max[-0]:
#                     max = j -i, j, i
#     print(max)
# maxProfit([1,2])

# one pass  okay
# def maxProfit(prices):
#     if len(prices) == 0:
#         return 0
#     tar, min = prices[0], 0
#     for index, i in enumerate(prices):
#         if i < tar:
#             tar = i
#         elif i - tar > min:
#             min = i - tar
#     print(min)
#
# maxProfit(test1)

"""
leetcode 122. Best Time to Buy and Sell Stock II

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
"""

# pass
# def maxProfit(prices):
#     total = 0
#     if len(prices) in [0, 1]:
#         return 0
#     for i in range(len(prices)-1):
#         temp = prices[i+1] - prices[i]
#         if temp > 0:
#             total = total + temp
#     print(total)
# maxProfit([7,6,4,3,1])

"""
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
"""
# wrong answer
# def maxProfit(prices):
#     max = 0
#     sec = 0
#     temp = 0
#     if len(prices) in [0, 1]:
#         return 0
#     for i in range(len(prices)-1):
#         inter = prices[i+1] - prices[i]
#         if inter > 0:
#             temp = temp + inter
#         else:
#             if temp > max:
#                 max, sec, temp = temp, max, 0
#             elif sec != 0 and temp > sec:
#                 sec, temp = temp, 0
#     print(max, sec, temp)
#     if temp > max:
#         max, sec, temp = temp, max, 0
#     elif temp > sec:
#         sec, temp = temp, 0
#     print(max + sec)
#
# maxProfit([1,2,4,2,5,7,2,4,9,0])

# Time Limit Exceeded but after I short(function short) the origin prices, it pass
# def maxProfit(prices):
#     total = 0
#     if len(prices) >3:
#         ans = [prices[0]]
#         for index, i in enumerate(prices[1:-1]):
#             if i == prices[index]:
#                 continue
#             if (i - prices[index]) * (prices[index + 2] - i) <= 0:
#                 ans.append(i)
#         ans.append(prices[-1])
#         prices = ans
#     def partition(slice):
#         if len(slice) == 0:
#             return 0
#         tar, min  = slice[0], 0
#         for index, i in enumerate(slice):
#             if i < tar:
#                 tar = i
#             elif i - tar > min:
#                 min  = i - tar
#         return min
#     for j in range(len(prices)-1):
#         tmp1 = partition(prices[:j])
#         tmp2 = partition(prices[j:])
#         tmp = tmp1 + tmp2
#         if tmp > total:
#             total = tmp
#     print(total)
# maxProfit([3,3,5,0,0,3,1,4])


# def short(a):
#     """
#     not perfect
#     :param a:
#     :return:
#     """
#     ans = [a[0]]
#     for index, i in enumerate(a[1:-1]):
#         if i == a[index]:
#             continue
#         if (i-a[index]) * (a[index+2]-i) <= 0:
#             ans.append(i)
#     ans.append(a[-1])
#     print(ans)
# short([1,1,2,4])

# best solution from comment
# def maxProfit(prices):
#     buy1 = float("inf")
#     sell1 = 0
#     buy2 = float("inf")
#     sell2 = 0
#     for p in prices:
#         buy1 = min(buy1, p)
#         sell1 = max(sell1, p-buy1)
#         buy2 = min(buy2, p-sell1)
#         sell2 = max(sell2, p-buy2)
#     print(buy1, sell1, buy2, sell2)
# maxProfit([3,3,5,0,0,3,1,4])

"""
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

"""
# pass
def maxProfit(k, prices):
    total = len(prices) // 2
    def fast(stocks):
        tmp = 0
        for index, i in enumerate(stocks[1:]):
            if i > stocks[index]:
                tmp = tmp+ i - stocks[index]
        return tmp
    if k > total:
        return fast(prices)
    if k == 0 or len(prices) == 0:
        return 0
    sell = [0 for _ in range(k)]
    buy = [float("inf") for _ in range(k)]
    for p in prices:
        for i in range(k):
            if i == 0:
                buy[i] = min(buy[i], p)
            else:
                buy[i] = min(buy[i], p - sell[i - 1])
            sell[i] = max(sell[i], p - buy[i])
    print(sell[-1])
maxProfit(0, [1])