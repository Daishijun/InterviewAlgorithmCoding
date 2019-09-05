#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/4 20:29
# @Author   : Daishijun
# @Site     : 
# @File     : helpothers.py
# @Software : PyCharm

# m, n = list(map(int,input().split()))
# arr = list(map(int,input().split()))
#
# resmax = max(arr)


def toneMerge(m,n,tone):
    dp = [[float('inf')]*n for i in range(m)]
    dp[0][0] = tone[0]
    for j in range(1,n):
        dp[0][j] = max(dp[0][j-1], tone[j])

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j], )

    return dp[0][n-1]
tone = [186, 64, 35, 32, 103]
print(toneMerge(tone))
