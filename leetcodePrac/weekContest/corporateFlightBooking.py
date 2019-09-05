#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/7 10:36
# @Author   : Daishijun
# @Site     : 
# @File     :
# @Software : PyCharm

'''Leetcode 周赛二题  航班预订统计'''

class Solution:
    def corpFlightBookings(self, bookings, n: int) :
        res = []
        tmpsum = [0]*(n+2)
        for start, end, num in bookings:
            tmpsum[start] += num
            tmpsum[end+1] -= num
        cur = 0
        for i in range(1, n+1):
            cur += tmpsum[i]
            res.append(cur)
        return res



if __name__ == '__main__':
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    S = Solution()
    print(S.corpFlightBookings(bookings, n))
