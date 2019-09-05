#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/30 11:26
# @Author   : Daishijun
# @Site     : 
# @File     : bookcaseHeight.py
# @Software : PyCharm

'''Leetcode 1105 填充书架 '''

class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:
        dp = [1<<31]*(len(books)+1)
        dp[0] = 0
        for i in range(1, len(dp)):
            curwid = 0    #最后一层目前累积的宽度
            lasth = 0    #最后一层的高度
            for j in range(i, 0, -1):
                curwid += books[j-1][0]
                if curwid>shelf_width:
                    break
                lasth = max(lasth, books[j-1][1])
                dp[i] = min(dp[i], dp[j-1]+lasth)
        return dp[-1]



