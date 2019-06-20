#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/16 17:27
# @Author   : Daishijun
# @Site     : 
# @File     : firstPosAndLastPosInSortedArr.py
# @Software : PyCharm

'''Leetcode 34 在排序数组中查找元素的第一个和最后一个位置'''


class Solution:
    def searchRange(self, nums, target: int) :
        if not nums or nums == []:
            return [-1, -1]
        length = len(nums)
        def getFirst(arr, target):
            l = 0
            r = len(arr)-1
            while l<=r:
                mid = (l+r)>>1
                if arr[mid] < target:
                    l = mid+1
                elif arr[mid] > target:
                    r = mid-1
                else :
                    if mid>0 and arr[mid-1] != target or mid == 0:
                        return mid
                    else:
                        r = mid -1
            return -1

        def getLast(arr, target):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = (l + r) >> 1
                if arr[mid] < target:
                    l = mid + 1
                elif arr[mid] > target:
                    r = mid - 1
                else:
                    if mid < len(arr)-1 and arr[mid + 1] != target or mid == len(arr)-1:
                        return mid
                    else:
                        l = mid + 1
            return -1


        return [getFirst(nums, target), getLast(nums, target)]
