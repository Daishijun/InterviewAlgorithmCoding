#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/18 21:18
# @Author   : Daishijun
# @Site     : 
# @File     : longestConsecutiveSequence.py
# @Software : PyCharm

'''Leetcode 128 最长连续序列'''

'''Leetcode 做法
将数组的转成set，然后遍历nums,如果数字i-1存在与set中，说明i不是一个连续序列的开头。
如果i-1不存在与set，说明i就是一个开头，查找是否i+1存在于set中，存在的话length+1.
'''
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

def longestConsecutive(arr):
    if not arr or len(arr) == 0:
        return 0
    maxlen = 1
    mapdict = {}
    for i in range(len(arr)):
        if arr[i] not in mapdict.keys():
            mapdict[arr[i]] = 1    #key==>元素数值， value==>这个数字所在的最长连续序列的长度
            if arr[i] - 1 in mapdict.keys():
                maxlen = max(maxlen, merge(mapdict, arr[i]-1, arr[i]))
            if arr[i] + 1 in mapdict.keys():
                maxlen = max(maxlen, merge(mapdict, arr[i], arr[i]+1))
    return maxlen

def merge(mapdict, less, more):   #更新记录
    left = less - mapdict[less]+1
    right = more + mapdict[more] -1
    length = right -left +1
    mapdict[left] = length
    mapdict[right] = length
    return length