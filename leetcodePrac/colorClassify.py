#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/16 18:26
# @Author   : Daishijun
# @Site     : 
# @File     : colorClassify.py
# @Software : PyCharm

'''Leetcode 75  颜色分类'''

'''
荷兰国旗问题
三指针。
'''

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zerop = 0
        cur = 0
        twop = len(nums)-1
        while cur <= twop:
            if nums[cur] == 0:
                nums[cur], nums[zerop] = nums[zerop], nums[cur]
                cur +=1
                zerop +=1
            elif nums[cur] == 2:
                nums[cur], nums[twop] = nums[twop], nums[cur]
                twop -=1
            else:
                cur +=1

if __name__ == '__main__':
    arr = [0,1,1,2,2,0,2,1,0]
    S = Solution()
    S.sortColors(arr)
    print(arr)