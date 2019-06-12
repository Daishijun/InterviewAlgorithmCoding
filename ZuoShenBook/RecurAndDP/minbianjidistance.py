# -*- coding: utf-8 -*-
# @Date    : 2019/4/18
# @Time    : 19:05
# @Author  : Daishijun
# @File    : minbianjidistance.py
# Software : PyCharm
'''
最小编辑距离
'''
'''
这里dp[i][j]的含义有些不同，因为要考虑空串，所以dp[i][j]不是对应str1[0...i]和str2[0...j],而是str1[0...i-1]。。。
'''
def minCost1(str1, str2, ic, dc, rc):
    if not str1 or not str2 :
        return 0
    chs1 = list(str1)
    chs2 = list(str2)
    rows = len(str1)+1
    cols = len(str2)+1
    dp = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(1, rows):
        dp[i][0] = dc*i
    for j in range(1, cols):
        dp[0][j] = ic*j
    for i in range(1, rows):
        for j in range(1, cols):
            if chs1[i-1] == chs2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + rc
            dp[i][j] = min(dp[i][j], dp[i][j-1]+ic)
            dp[i][j] = min(dp[i][j], dp[i-1][j]+dc)
    return dp[-1][-1]



if __name__ == '__main__':
    str1 = 'ab12cd3'
    str2 = 'abcdf'
    print(minCost1(str1, str2, 5,3,2))
