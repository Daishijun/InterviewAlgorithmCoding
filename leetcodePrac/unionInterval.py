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
        intervals.sort()    #根据start排序，这样多个相同的start或者start在之前的区间内的，就可以直接将区间扩展了。
        resdict = {}   #保存key：区间start， value：区间end
        start = 0
        right = 0
        for pari in intervals:
            if resdict == {} or right<pari[0]:    #为空或者当前的区间与之前的区间不相交
                resdict[pari[0]] = pari[1]
                right = pari[1]    #更新目前的右边界
                start = pari[0]    #更新新区间的start
            else:
                resdict[start] = max(resdict[start], pari[1])
                right = resdict[start]
        res = []
        for key, val in resdict.items():
            res.append([key, val])
        return res
