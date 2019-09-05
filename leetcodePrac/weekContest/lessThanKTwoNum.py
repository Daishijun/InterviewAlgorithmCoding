#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/29 22:30
# @Author   : Daishijun
# @Site     : 
# @File     : lessThanKTwoNum.py
# @Software : PyCharm

'''Leetcode 1'''

class Solution:
    def twoSumLessThanK(self, A, K: int) -> int:
        if not A or A == [] or len(A)<2:
            return -1
        res = -1
        A.sort()
        left = 0
        right = len(A)-1
        while left< right:
            if A[left]+A[right] >= K :
                right -=1
            else:
                res = max(res, A[left]+A[right])
                left +=1
        return res

if __name__ == '__main__':
    S = Solution()
    # A = [34,23,1,24,75,33,54,8]
    A =  [10,20,30]
    # K = 60
    K = 15
    print(S.twoSumLessThanK(A,K))