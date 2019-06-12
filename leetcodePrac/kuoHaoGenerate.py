# -*- coding: utf-8 -*-
# @Date    : 2019/6/9
# @Time    : 23:24
# @Author  : Daishijun
# @File    : kuoHaoGenerate.py
# Software : PyCharm

'''Leetcode 22 括号生成'''
'''
回溯法
溯源算法可以理解为是一种试探性的全局搜索。
穷举出每一种可能性，把所有成功的解都返回解空间的一种算法。
'''

class Solution:
    def generateParenthesis(self, n: int):
        res = []
        self.backtrack(n, n, '', res)
        return res

    def backtrack(self, left, right, tmp, res):
        if left == 0 and right == 0:
            res.append(tmp)
            return res
        if left > 0:
            self.backtrack(left - 1, right, tmp + '(', res)
        if right > left:
            self.backtrack(left, right - 1, tmp + ')', res)

if __name__ == '__main__':
    dic = {}
    dic[(0,1,0)] = 'abc'
    dic[(1,1,1)] = 'cbd'
    print(dic)