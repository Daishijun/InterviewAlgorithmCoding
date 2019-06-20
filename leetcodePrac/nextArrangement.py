#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/17 17:41
# @Author   : Daishijun
# @Site     : 
# @File     : nextArrangement.py
# @Software : PyCharm

'''Leetcode 31 下一个排列'''

'''!!!想不出来方法。!!!'''
'''Leetcode 官方解答的方法很牛，主要还是规律没有找到(既有交换，又有部分逆序)'''


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reversepart(arr):
            return arr[::-1]
        for ind in range(len(nums)-1, 0, -1):
            if nums[ind-1] < nums[ind]:
                break
        if nums[ind-1] >= nums[ind]:
            nums = nums[::-1]
        else:
            for j in range(ind, len(nums)):
                if nums[j] > nums[ind-1]:
                    break
            nums[ind-1], nums[j] = nums[j], nums[ind-1]
            nums[ind:] = reversepart(nums[ind:])

