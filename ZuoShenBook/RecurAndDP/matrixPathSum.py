# -*- coding: utf-8 -*-
# @Date    : 2019/4/28
# @Time    : 18:59
# @Author  : Daishijun
# @File    : matrixPathSum.py
# Software : PyCharm
'''
矩阵的最小路径和
'''

def minPathSum1(mat):
    if not mat or len(mat) <1 or len(mat[0])<1:
        return 0
    rows = len(mat)
    cols = len(mat[0])
    dp = [[0 for i in range(cols)] for j in range(rows)]
    dp[0][0] = mat[0][0]
    for j in range(1,cols):
        dp[0][j] = dp[0][j-1]+mat[0][j]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + mat[0][i]
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + mat[i][j]
    return dp[rows-1][cols-1]

if __name__ =='__main__':
    mat = [[1,3,5,9],[8,1,3,4],[5,0,6,1],[8,8,4,0]]
    print(minPathSum1(mat))