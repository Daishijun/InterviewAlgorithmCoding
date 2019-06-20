#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/16 16:18
# @Author   : Daishijun
# @Site     : 
# @File     : sumKSubArr.py
# @Software : PyCharm

'''Leetcode 560 和为K的子数组'''

'''
用hash表来存每个sum出现的次数。只需要遍历一次nums就行。
'''

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        count = 0
        mapdict = {0: 1}
        tmpsum = 0
        for num in nums:
            tmpsum += num
            if tmpsum - k in mapdict.keys():
                count += mapdict[tmpsum - k]

            mapdict[tmpsum] = mapdict.get(tmpsum, 0) + 1
        return count
