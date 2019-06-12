# -*- coding: utf-8 -*-
# @Date    : 2019/6/10
# @Time    : 12:48
# @Author  : Daishijun
# @File    : combineSum.py
# Software : PyCharm

'''Leetcode 39 组合总和'''
'''
回溯算法
'''


class Solution:
    def combinationSum(self, candidates, target: int) :
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target:
                    break
                backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])

        backtrack(0, 0, [])
        return res


class Solution:
    def combinationSum(self, candidates, target: int) :
        candidates.sort()
        res = []
        def backtrack(index, curtar, path):
            if curtar > target or index == len(candidates):
                return
            if curtar == target:
                res.append(path)
                return
            for j in range(index, len(candidates)):
                if curtar+candidates[j] > target:
                    break
                backtrack(j, curtar+candidates[j], path+[candidates[j]])
        backtrack(0, 0, [])
        return res
