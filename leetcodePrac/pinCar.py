#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/23 11:17
# @Author   : Daishijun
# @Site     : 
# @File     : pinCar.py
# @Software : PyCharm

'''Leetcode 1094'''

class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        res = True
        outstack = []
        capcur = 0
        trips.sort(key = lambda x:(x[1], x[2]))
        print('trips:', trips)
        for trip in trips:
            while outstack and outstack[0][-1] <= trip[1]:
                capcur -= outstack[0][0]
                outstack.pop(0)
            capcur += trip[0]
            outstack.append(trip)
            outstack.sort(key=lambda x:x[2])
            if capcur > capacity:
                res = False
                break
            print('stack:', outstack)
        return res

if __name__ == '__main__':
    S = Solution()
    # trips = [[3,2,7],[3,7,9],[8,3,9]]
    # trips =  [[2,1,5],[3,5,7]]
    # trips =  [[9,3,6],[8,1,7],[6,6,8],[8,4,9],[4,2,9]]
    cap = 28
    print(S.carPooling(trips, cap))