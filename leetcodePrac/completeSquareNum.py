#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/26 19:20
# @Author   : Daishijun
# @Site     : 
# @File     : completeSquareNum.py
# @Software : PyCharm

'''Leetcode 279 完全平方数'''

'''
四平方定理
任意一个正整数可以表示成不超过四个整数的平方和的形式
满足四平方（即最少拆分成4个整数平方和）的整数n，必然满足n = 4 ^(a*(8*b+7))
'''

class Solution:
    def numSquares(self, num: int) -> int:
        while num%4 == 0:
            num//=4
        if num%8 == 7:
            return 4
        a = 0
        while a**2 <=num:    #暴力看能不能拆成两个平方数的和
            b = int((num-a**2)**0.5)
            if a**2 + b**2 == num:
                return (not not a) + (not not b)
            a +=1
        return 3

'''

'''