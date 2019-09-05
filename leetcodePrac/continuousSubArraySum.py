#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/1 21:44
# @Author   : Daishijun
# @Site     : 
# @File     : continuousSubArraySum.py
# @Software : PyCharm

'''Leetcode 523'''

'''类似于左神page384， 用累加和，hashmap来做。'''
'''
        /**
        在每个索引位置i, 计算当前和对k的mod值, 假设在索引x处, sum[0~x] = m*k + mod_x;
        在索引y处, sum[0~y] = n*k + mod_y; 如果mod_x == mod_y且y-x > 1说明sum[x~y]
        即为一个符合要求的连续子数组, 用map来保存每个mod值对应的索引, 一旦出现新的mod值出现
        在map中, 判断索引差是否大于1.
        注意特殊情况: 
        1) 当nums中有连续0, 无论k为何值都是正确的;
        2) 除情况1之外出现k为0都是错误的;
        3) k为负数也是可能的, 但是要将其变为对应正数来求mod.
        此外需要在map中初始化<0,-1>, 其原因在于解决到达某个i时sum恰好可以整除k的情况, 选择-1
        的原因是要求连续子数组长度大于等于2, 这样可以避免第一个数字为0的情况
        **/
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] and nums[i] == 0:
                return True
        if k == 0:
            return False
        mapdict = {0: -1}
        tmpsum = 0
        for i in range(len(nums)):
            tmpsum += nums[i]
            yushu = tmpsum % k
            if yushu in mapdict.keys():
                if i - mapdict[yushu] >= 2:
                    return True
            else:
                mapdict[yushu] = i
        # for k,v in mapdict.items():
        #     print(k,':',v)
        return False




'''暴力解'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] and nums[i] == 0:
                return True
        if k == 0:
            return False
        for i in range(len(nums)):
            cursum = nums[i]
            for j in range(i+1, len(nums)):
                cursum += nums[j]
                if cursum%k == 0:
                    return True
        return False