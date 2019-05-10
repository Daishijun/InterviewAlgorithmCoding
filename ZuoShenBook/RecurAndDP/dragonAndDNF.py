# -*- coding: utf-8 -*-
# @Date    : 2019/4/18
# @Time    : 19:39
# @Author  : Daishijun
# @File    : dragonAndDNF.py
# Software : PyCharm
'''
龙与地下城
'''

def minHP1(m):
    if not m:
        return 1
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
            right = max(dp[i][j+1]-m[i][j], 1)
            down = max(dp[i+1][j-1]-m[i][j],1)
            dp[i][j] = min(right,down)
    return dp[0][0]



if __name__ == '__main__':
    m=[[-2,-3,3],[-5,-10,1],[0,30,-5]]
    print(minHP1(m))
