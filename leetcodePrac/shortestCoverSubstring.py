#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/26 14:39
# @Author   : Daishijun
# @Site     : 
# @File     : shortestCoverSubstring.py
# @Software : PyCharm

'''Leetcode 76 最小覆盖子串'''

'''
双指针，变长窗口。用字典统计需要匹配的子串的词频，另一个字典统计窗口内的词频，
如果待匹配子串的词频和窗口内的词频相等，说明目前窗口内可以包含子串，固定right指针
left ++ 缩小窗口。不满足词频相等时候，right++，进入下一次大循环。
'''
class Solution:
    def minWindow(self, string: str, substr: str) -> str:
        if not string or not substr or len(string)<len(substr):
            return ''
        left = 0
        right = 0
        subdict = {}
        for s in substr:
            subdict[s] = subdict.get(s, 0)+1
        letternum = len(subdict)

        ans = (float('inf'), None, None)
        letflag = 0
        windowdict = {}
        while right < len(string):
            cur = string[right]
            windowdict[cur] = windowdict.get(cur, 0)+1
            if cur in subdict.keys() and windowdict[cur] == subdict[cur]:
                letflag +=1
            while left<= right and letflag == letternum:
                cur = string[left]
                curlen = right-left+1
                if curlen < ans[0]:
                    ans = (curlen, left, right)
                windowdict[cur] -=1
                if cur in subdict.keys() and windowdict[cur] < subdict[cur]:
                    letflag -=1
                left +=1
            right +=1
        return '' if ans[0] == float('inf') else \
            string[ans[1]:ans[2]+1]