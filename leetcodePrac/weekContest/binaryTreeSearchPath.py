#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/30 10:55
# @Author   : Daishijun
# @Site     : 
# @File     : binaryTreeSearchPath.py
# @Software : PyCharm

'''Leetcode 1103 二叉树寻路 '''

class Solution:
    def pathInZigZagTree(self, label: int):
        restmp = []
        aim = label
        while aim>0:
            restmp.append(aim)
            aim = aim>>1

        # print(restmp[::-1])
        restmp = restmp[::-1]
        length = len(restmp)

        for i in range(length-2, 0, -2):
            restmp[i] = 2**(i)+(2**(i+1)-1-restmp[i])
        # print('changed:', restmp)
        return restmp


if __name__ == '__main__':
    S = Solution()
    label = 26
    print(S.pathInZigZagTree(label))