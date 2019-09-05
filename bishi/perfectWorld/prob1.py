#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/23 17:42
# @Author   : Daishijun
# @Site     : 
# @File     : prob1.py
# @Software : PyCharm

def minHP1(m):

    rows = len(m)
    cols = len(m[0])
    dp = [[0 for i in range(cols)] for j in range(rows)]
    dp[rows-1][cols-1] = 1 if m[rows-1][cols-1]>0 else -m[rows-1][cols-1]+1
    for j in range(cols-2, -1,-1):
        dp[rows-1][j] = max(dp[rows-1][j+1]-m[rows-1][j], 1)
    right = 0
    down = 0
    for i in range(rows-2, -1, -1):
        dp[i][cols-1] = max(dp[i+1][cols-1]-m[i][cols-1], 1)
    for i in range(rows-2, -1, -1):
        for j in range(cols-2,-1,-1):
            right = max(dp[i][j+1]-m[i][j], 1)    #和1取最大是为了排除加血可能产生的影响。
            down = max(dp[i+1][j-1]-m[i][j],1)
            dp[i][j] = min(right,down)
    return dp[0][0]

# n = int(input())
# m = int(input())
# mat = [[0]*m for i in range(n)]
#
# matflatten = list(map(int, input().split()))
#
#
#
# k = 0
# for i in range(n):
#     for j in range(m):
#         mat[i][j] = matflatten[k]
#         k +=1
#
# for i in range(n):
#     print(mat[i])
# print(mat)

def minHP2(mat):
    n = len(mat)
    m = len(mat[0])
    dp = [[0]*m for i in range(n)]
    dp[-1][-1] = max(1-mat[-1][-1], 1)

    for i in range(m-2, -1,-1):
        dp[-1][i] = max(1, dp[-1][i+1]-mat[-1][i])
    for i in range(n-2, -1, -1):
        dp[i][-1] = max(1, dp[i+1][-1]-mat[i][-1])
    for i in range(n-2, -1,-1):
        for j in range(m-2, -1, -1):
            dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-mat[i][j], 1)
    print(dp)
    return dp[0][0]

mat = [[-2, -3, 3],
       [-5, -10, 1],
       [0, 30, -5]]
inputmat = [[0]*3 for _ in range(3)]
flattenmat = [-2,-3,3,-5,-10,1,0,30,-5]

k = 0
for i in range(3):
    for j in range(3):
        inputmat[i][j] = flattenmat[k]
        k +=1
print(inputmat)

print(minHP2(inputmat))
print(minHP1(inputmat))

