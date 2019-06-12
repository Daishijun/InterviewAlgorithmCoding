# -*- coding: utf-8 -*-
# @Date    : 2019/6/10
# @Time    : 13:46
# @Author  : Daishijun
# @File    : phoneNumberLetterCombine.py
# Software : PyCharm

'''Leetcode 17  电话号码的字母组合'''


class Solution:
    def letterCombinations(self, digits: str) :
        if not digits or len(digits) == 0:
            return []
        letterlist = [['a','b','c'],['d','e','f'], ['g','h','i'],
                      ['j','k','l'],['m','n','o'],['p','q','r','s'],
                      ['t','u','v'],['w','x','y','z']]
        n = len(digits)
        res=  []
        def backtrack(index, path):
            if index == n:
                res.append(path)
                return
            digitind = ord(digits[index]) - ord('2')
            for s in letterlist[digitind]:
                backtrack(index+1, path+s)
        backtrack(0, '')
        return res


#算是BFS，宽度优先遍历
class Solution:
    def letterCombinations(self, digits: str):
        m = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz'),
            }
        if not digits: return []
        ls1 = ['']
        for i in digits:
            ls1 = [x + y for x in ls1 for y in m[i]]
        return ls1

