#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/1 16:29
# @Author   : Daishijun
# @Site     : 
# @File     : p3.py
# @Software : PyCharm

'''n个骰子，求最大值期望'''
'''
用DP，dp[i][j]表示用前i个骰子，最大值为j的情况数量
'''

n = int(input())
nlist = list(map(int, input().split()))

def getdp(nlist):
    dp = [[0]* (max(nlist)+1) for i in range(len(nlist)+1)]
    for i in range(1,nlist[0]+1):
        dp[1][i] = 1
    maxmum = nlist[0]
    for i in range(2, len(dp)):
        maxmum = max(maxmum, nlist[i-1])
        for j in range(1, maxmum+1):
            if j<=nlist[i-1]:
                dp[i][j] = dp[i-1][j]*(j-1) + sum(dp[i-1][:j+1])    #分别是第i个骰子取不到最大值j，此时需要前i-1个骰子取到j，或者第i个取到j，则前i-1个只要不大于j就行。
            else:
                dp[i][j] = dp[i-1][j]*nlist[i-1]    #最大值在前i-1个取到，第i个取不到这个最大值。
    return dp

totalsum = 0
divid = 0
dp = getdp(nlist)
print(dp)
for j in range(1, max(nlist)+1):
    totalsum += j*dp[n][j]
    divid +=dp[n][j]

print('{0:.3}'.format(totalsum/divid))
