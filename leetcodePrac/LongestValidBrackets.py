# -*- coding: utf-8 -*-
# @Date    : 2019/6/9
# @Time    : 12:48
# @Author  : Daishijun
# @File    : LongestValidBrackets.py
# Software : PyCharm

'''Leetcode 32 最长有效括号'''
'''
dp[i]表示以string[i]为结尾的情况下，最长合法括号字符串长度。
'''

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s or len(s) <2:
            return 0
        dp = [0 for i in range(len(s))]
        res= 0
        for i in range(1, len(dp)):
            if s[i] == ')':
                pre = i- dp[i-1]-1
                if pre >=0 and s[pre] == '(':
                    dp[i] = dp[i-1]+2 + (dp[pre-1] if pre>0 else 0)
            res = max(res, dp[i])
        return res
