#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/23 19:14
# @Author   : Daishijun
# @Site     : 
# @File     : prob2.py
# @Software : PyCharm

N = int(input())
coinlist = list(map(int, input().split()))

target = int(input())

def minCoins_dp(arr, aim):
    if not arr or aim<0:
        return -1
    dp = [[-1 for i in range(aim+1)] for j in range(len(arr)+1)]
    dp[len(arr)][0] = 0
    for i in range(len(arr)-1, -1,-1):
        for j in range(0, aim+1):
            if dp[i+1][j] !=-1:
                dp[i][j] = dp[i+1][j]
            if j-arr[i] >=0 and dp[i][j-arr[i]] !=-1:    #在j的循环中实际上就是遍历了对于arr[i]面额选择0--最多张的情况。
                if dp[i+1][j] ==-1:
                    dp[i][j] = dp[i][j-arr[i]]+1
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-arr[i]]+1)

    return dp[0][aim]



print(minCoins_dp(coinlist, target))