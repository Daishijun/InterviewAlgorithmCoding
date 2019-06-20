#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/18 21:18
# @Author   : Daishijun
# @Site     : 
# @File     : longestConsecutiveSequence.py
# @Software : PyCharm

'''Leetcode 128 最长连续序列'''


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxlen = 1
        mapset = set(nums)
        for num in nums:
            if num - 1 not in mapset:
                cur = num
                curlen = 1
                while cur + 1 in mapset:
                    cur = cur + 1
                    curlen += 1
                maxlen = max(maxlen, curlen)

        return maxlen