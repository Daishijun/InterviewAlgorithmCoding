# -*- coding: utf-8 -*-
# @Date    : 2019/6/13
# @Time    : 15:33
# @Author  : Daishijun
# @File    : mostWaterDocker.py
# Software : PyCharm

'''Leetcode 11 盛最多水的容器'''
'''
这道题和左神书里的题并不一样，这个相当于在每个位置点插入一个板, 找能盛水最多的两个板之间的盛水量
'''

class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height)-1
        resmax = 0
        while left < right:
            resmax = max(resmax, min(height[left], height[right])*(right-left))
            if height[left]<=height[right]:
                left+=1
            else:
                right -=1
        return resmax

if __name__ == '__main__':
    import numpy as np
    print(np.array([1,2,3]))
