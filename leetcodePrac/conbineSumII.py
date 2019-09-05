# -*- coding: utf-8 -*-
# @Date    : 2019/6/10
# @Time    : 13:22
# @Author  : Daishijun
# @File    : conbineSumII.py
# Software : PyCharm

'''Leetcode 40 组合总和II'''


class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        res = []

        def backtrack(index, cursum, path):

            if cursum==target:
                res.append(path)
                return
            prenums = []
            for j in range(index, len(candidates)):
                num = candidates[j]
                if num in prenums:
                    continue
                if cursum+num > target:
                    break
                prenums.append(num)
                backtrack(j+1, cursum+num, path+[num])
        backtrack(0, 0, [])
        return res

if __name__ == '__main__':
    S = Solution()
    print('???')