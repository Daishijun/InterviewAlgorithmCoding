#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/16 11:20
# @Author   : Daishijun
# @Site     : 
# @File     : labelMax.py
# @Software : PyCharm

'''Leetcode 141周赛 第2题： 受标签影响的最大值'''

'''
贪心，把两个list绑在一起根据value排序。然后从最大值开始选，需要注意可能选不到最大数量，所以在遍历
到末尾时需要break。
'''

class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted: int, use_limit: int) -> int:
        values, labels = (list(t) for t in zip(*sorted(zip(values, labels), reverse=True)))
        countmap = {}
        res = 0
        ind = 0
        while num_wanted:
            countmap[labels[ind]] = countmap.get(labels[ind], 0) + 1
            if countmap[labels[ind]] <= use_limit:
                res += values[ind]
                num_wanted -=1
            ind +=1
            if ind == len(values):
                break
        return res

if __name__ == '__main__':
    values = [5, 4, 3, 2, 1]; labels = [1, 1, 2, 2, 3]; num_wanted = 3; use_limit = 1
    values = [5, 4, 3, 2, 1]; labels = [1, 3, 3, 3, 2]; num_wanted = 3; use_limit = 2
    values = [9, 8, 8, 7, 6]; labels = [0, 0, 0, 1, 1]; num_wanted = 3; use_limit = 1
    values = [9, 8, 8, 7, 6]; labels = [0, 0, 0, 1, 1]; num_wanted = 3; use_limit = 2
    S = Solution()
    print(S.largestValsFromLabels(values, labels, num_wanted, use_limit))

