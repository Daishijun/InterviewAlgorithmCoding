#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/31 16:34
# @Author   : Daishijun
# @Site     : 
# @File     : xinlang.py
# @Software : PyCharm

nums = list(map(int, input().split(',')))

def minMove(nums):
    if len(nums)<2:
        return 0
    nums.sort()
    res = 0
    prenum = nums[0]
    for i in range(1,len(nums)):
        if nums[i] <= prenum:
            res += prenum-nums[i]+1
            prenum +=1
        else:
            prenum = nums[i]

    return res

print(minMove(nums))

