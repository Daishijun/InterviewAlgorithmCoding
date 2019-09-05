#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/30 10:33
# @Author   : Daishijun
# @Site     : 
# @File     : candiesII.py
# @Software : PyCharm

'''Leetcode 1104 分糖果II '''

class Solution:
    def distributeCandies(self, candies: int, num_people: int) :
        if not candies or candies == [] or num_people <1:
            return []
        res = [0]*num_people
        addp = 0
        while candies>0:
            for i in range(num_people):
                if candies >= i+1+addp:
                    res[i] += i+1+addp
                    candies -=i+1+addp
                else:
                    res[i] += candies
                    candies -=i+1+addp
                if candies<=0:
                    break
            addp+=num_people
        return res

if __name__ == '__main__':
    cand = 10
    num = 3
    S = Solution()
    print(S.distributeCandies(cand,num))


