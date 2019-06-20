#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/16 14:50
# @Author   : Daishijun
# @Site     : 
# @File     : shortestCommonSuperSeq.py
# @Software : PyCharm

'''LeetCode 141周赛 题目4： 最短公共超序列'''
'''
思路是先找两个字符串的最长公共子序列，‘xxxx’然后从头比较，不等于公共子序列当前位置的字符，说明不在公共区域内，
需要单独添加。
最后当公共区域比较完了之后，把两个字符串的剩余部分加到后面
'''


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if not str1 or not str2 :
            return None
        if str1 == '':
            return str2
        if str2 == '':
            return str1
        len1 = len(str1)
        len2 = len(str2)
        def getdp(str1, str2):
            dp = [[0] * len2 for _ in range(len1) ]
            dp[0][0] = 1 if str1[0] == str2[0] else 0
            for i in range(1,len1):
                dp[i][0] = max(dp[i-1][0], 0 if str1[i] !=str2[0] else 1)
            for j in range(1, len2):
                dp[0][j] = max(dp[0][j-1], 0 if str1[0] != str2[j] else 1)
            for i in range(1, len1):
                for j in range(1, len2):
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    if str1[i] == str2[j]:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
            return dp
        def longestcommonSeq(str1, str2, dp):
            res = ['']* dp[-1][-1]
            index = len(res)-1
            i = len1-1
            j = len2-1
            while index>-1:
                if i>0 and dp[i][j] == dp[i-1][j]:
                    i -=1
                elif j>0 and dp[i][j] == dp[i][j-1]:
                    j -=1
                else:
                    res[index] = str1[i]
                    index -= 1
                    i -=1
                    j -=1
            return res
        dp = getdp(str1, str2)
        common = longestcommonSeq(str1, str2, dp)
        cind = 0
        ind1 = 0
        ind2 = 0
        res = []
        while cind < len(common):
            while ind1<len1 and str1[ind1] != common[cind]:
                res.append(str1[ind1])
                ind1 +=1
            while ind2<len2 and str2[ind2] != common[cind]:
                res.append(str2[ind2])
                ind2 +=1
            res.append(common[cind])
            cind +=1
            ind1 +=1
            ind2 +=1
        while ind1<len1:
            res.append(str1[ind1])
            ind1 +=1
        while ind2 < len2:
            res.append(str2[ind2])
            ind2 +=1
        return ''.join(res)


