# -*- coding: utf-8 -*-
# @Date    : 2019/4/25
# @Time    : 14:02
# @Author  : Daishijun
# @File    : huiwenMinCut.py
# Software : PyCharm
'''
回文最少分割数
'''
#把给定字符串string全部切成回文子串，求最小切割次数

'''
    动态规划，涉及两个dp数组，一个是最小分割数，一个是是否构成回文。
'''

def minCut(string):
    if not string or string=='':
        return 0
    dp = [0 for i in range(len(string)+1)]    #多设置一个元素，dp最后位置设置成-1，这样可以避免越界问题。
    pmat = [[0 for i in range(len(string))] for j in range(len(string))]

    dp[-1] = -1
    for i in range(len(string)-1, -1, -1):
        dp[i] = float('inf')
        for j in range(i, len(string)):
            if string[i]==string[j] and (j-i <2 or pmat[i+1][j-1]):
                pmat[i][j] = 1    #string[i:j+1]是回文串。
                dp[i] = min(dp[i], dp[j+1]+1)    #如果不多设置一个元素的话，这里需要根据j是否处于最后一个位置，分情况定义。
        print('dp[{i}]={dp}'.format(i=i, dp=dp[i]))
    return dp[0]

if __name__ == '__main__':
    string = 'aba'
    print(minCut(string))
    print(string.encode('one-hot'))