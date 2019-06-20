#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/19 9:55
# @Author   : Daishijun
# @Site     : 
# @File     : removeInvalidParentheses.py
# @Software : PyCharm

'''Leetcode 301   删除无效括号'''

'''
统计左右括号，如果不多的话，left==right==0，如果左括号多，则left>0,右括号多，则right>0
然后从头开始遍历，dfs删除第i位置的符号，如果left==right==0，然后从头检查是否合法。
dfs中需要去重，当两个符号相同时直接跳过第二个就行了
'''

class Solution:
    def removeInvalidParentheses(self, s: str) :

        res = []
        left = 0
        right = 0

        def dfs(string, start, left, right):
            if left == 0 and right == 0:
                if check(string):
                    res.append(string)
            for i in range(start, len(string)):    #从start位置开始往后遍历，前面的已经合法了。
                if i - 1 >= start and string[i] == string[i - 1]:
                    continue
                if left > 0 and string[i] == '(':
                    dfs(string[:i] + string[i + 1:], i, left - 1, right)    #start的遍历位置从i开始，因为前面i-1个字符已经使合法的了
                if right > 0 and string[i] == ')':
                    dfs(string[:i] + string[i + 1:], i, left, right - 1)

        def check(string):
            left = 0
            for s in string:
                if s == '(':
                    left += 1
                elif s == ')':
                    left -= 1
                    if left < 0:
                        return False
            return left == 0

        for ss in s:
            if ss =='(':
                left +=1
            elif ss == ')':
                if left>0:
                    left -=1
                else:
                    right +=1
        dfs(s, 0 , left, right)
        return res


