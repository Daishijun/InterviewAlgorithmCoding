# -*- coding: utf-8 -*-
# @Date    : 2019/6/1
# @Time    : 17:31
# @Author  : Daishijun
# @File    : stringCrossMakeup.py
# Software : PyCharm

'''
字符串的交错组成，
给定3个字符串，判断是否aim 串可以由str1 和str2 交错组成。
'''

def isCross(str1, str2, aim):
    if not str1 or not str2 or not aim:
        return False
    if len(aim) !=len(str1) + len(str2):
        return False
    dp = [[False for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    dp[0][0] = True
    for i in range(1, len(str1)+1):
        if str1[i-1] != aim[i-1]:
            break

        dp[i][0] = True
    for j in range(1, len(str2)+1):
        if str2[j-1] != aim[j-1]:
            break
        dp[0][j] = True
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if (str1[i-1] == aim[i+j-1] and dp[i-1][j]) or (str2[j-1] == aim[i+j-1] and dp[i][j-1]):
                dp[i][j] = True
    return dp[-1][-1]


