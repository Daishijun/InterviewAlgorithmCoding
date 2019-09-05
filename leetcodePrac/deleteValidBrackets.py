#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/26 14:59
# @Author   : Daishijun
# @Site     : 
# @File     : deleteValidBrackets.py
# @Software : PyCharm

'''Leetcode 301 删除无效的括号'''

'''dfs, 有回溯思想'''

class Solution:
    def removeInvalidParentheses(self, s: str) :
        left = 0    #左括号多了多少，
        right = 0    #右括号多了多少
        res = []
        for ss in s :
            if ss == '(':
                left +=1
            elif ss == ')':
                if left>0:
                    left -=1
                else :
                    right +=1
        def check(string):
            left = 0
            for ss in string:
                if ss == '(':
                    left +=1
                elif ss == ')':
                    left -=1
                    if left <0:
                        return False
            return left == 0
        def dfs(string, startind, left, right):
            if left == 0 and right == 0:
                if check(string):
                    res.append(string)
            for i in range(startind, len(string)):
                if i-1>=startind and string[i] == string[i-1]:
                    continue
                if left>0 and string[i] == '(':  #正好左括号多，目前的i位置还是左括号，那么就可以删去然后做dfs
                    dfs(string[:i]+string[i+1:], i, left-1, right)
                if right>0 and string[i] == ')':
                    dfs(string[:i]+string[i+1:], i, left, right-1)
        dfs(s, 0, left, right)
        return res