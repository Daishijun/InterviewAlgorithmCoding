#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/19 12:43
# @Author   : Daishijun
# @Site     : 
# @File     : searchMidInTwoSortedArr.py
# @Software : PyCharm


'''Leetcode 4 寻找两个有序数组的中位数'''

'''
这里是根据根据长串中的位置i，和两个List的总长度的一半，来计算出j，这样就保证考察的划分方式保持是中位数。

'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m = len(nums1)
        n = len(nums2)
        if m>n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            raise Exception('One None')
        imin, imax, halflen = 0, m, (m+n+1)//2    #二分初始位置， 两个list的一半位置。
        while imin<= imax:
            i = (imin+imax)>>1
            j = halflen - i
            if i<m and nums2[j-1] > nums1[i]:
                imin = i+1
            elif i>0 and nums1[i-1] > nums2[j]:
                imax = i-1
            else:
                if i == 0:
                    maxofleft = nums2[j-1]
                elif j == 0:
                    maxofleft = nums1[i-1]
                else:
                    maxofleft = max(nums1[i-1], nums2[j-1])

                if (m+n)&1:
                    return float(maxofleft)

                if i == m:
                    minofright = nums2[j]
                elif j == n:
                    minofright = nums1[i]
                else:
                    minofright = min(nums1[i], nums2[j])

                return (maxofleft + minofright)/2.0
        return 0.0