#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/17 17:06
# @Author   : Daishijun
# @Site     : 
# @File     : unionInterval.py
# @Software : PyCharm

'''Leetcode 56 合并区间'''
class Solution:
    def merge(self, intervals) :
        intervals.sort()
        resdict = {}
        start = 0
        right = 0
        for pari in intervals:
            if resdict == {} or right<pari[0]:
                resdict[pari[0]] = pari[1]
                right = pari[1]
                start = pari[0]
            else:
                resdict[start] = max(resdict[start], pari[1])
                right = resdict[start]
        res = []
        for key, val in resdict.items():
            res.append([key, val])
        return res
