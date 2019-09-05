# -*- coding: utf-8 -*-
# @Date    : 2019/4/24
# @Time    : 14:41
# @Author  : Daishijun
# @File    : addCharChangetoHuiwen.py
# Software : PyCharm
'''
添加最少字符使字符串整体都是回文字符串
'''
#动态规划，dp[i][j]表示将原始str[i...j]变成回文字符串最少需要添加的字符数量。,因为i<=j，所以dp矩阵只有上三角有用。

def getDP(string):
    dp = [[0 for i in range(len(string))] for j in range(len(string))]
    for j in range(1, len(string)):
        dp[j-1][j] = 0 if string[j-1]==string[j] else 1
        for i in range(j-2, -1, -1):
            if string[i]==string[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1])+1
    return dp

def getPalindromel(string):
    if not string or len(string)<2:
        return string
    dp = getDP(string)
    res = [0 for i in range(len(string)+dp[0][len(string)-1])]
    si = 0; sj=len(string)-1
    resl = 0; resr = len(res)-1
    while si<= sj:
        if string[si]==string[sj]:
            res[resl] = string[si]
            res[resr] = string[si]
            resl +=1; resr -=1
            si +=1;  sj-=1
        elif dp[si+1][sj] <dp[si][sj-1]:
            res[resl] = string[si]
            res[resr] = string[si]
            resl +=1; resr -=1
            si +=1
        else:
            res[resl] = string[sj]
            res[resr] = string[sj]
            resl +=1; resr-=1
            sj -=1
    print(res)
    return ''.join(res)


### 进阶问题， 额外给出给定字符串string的最长回文子序列。仍然求添加最少字符情况下，使字符串变成回文的结果。

### 剥洋葱， 给出的最长回文子序列相当于每一层的洋葱。
def setres(res, resL, resR, string, tmpL, stringL, stringR, tmpR):
    for i in range(tmpL, stringL):
        res[resL] = string[i]
        res[resR] = string[i]
        resL +=1; resR-=1
    for j in range(tmpR, stringR, -1):
        res[resL] = string[j]
        res[resR] = string[j]
        resL +=1
        resR -=1


def getPalindrome2(string, strlps):
    if not string or string=='':
        return ''
    res = [0 for i in range(2*len(string)- len(strlps))]
    resl = 0
    resr = len(res)-1
    stringL = 0
    stringR = len(string)-1
    strlpsL = 0
    strlpsR = len(strlps)-1
    while strlpsL<=strlpsR:
        tmpL = stringL
        tmpR = stringR
        while string[stringL]!=strlps[strlpsL]:
            stringL +=1
        while string[stringR] !=strlps[strlpsR]:
            stringR -=1
        setres(res, resL=resl, resR=resr, string=string, tmpL=tmpL, stringL=stringL, stringR=stringR, tmpR=tmpR)
        resl += stringL-tmpL+tmpR- stringR
        resr -= stringL-tmpL+tmpR- stringR
        res[resl] = string[stringL]
        res[resr] = string[stringR]
        stringL +=1
        stringR -=1
        resl +=1
        resr -=1
        strlpsL +=1
        strlpsR -=1
    return ''.join(res)



if __name__ == '__main__':
    string = 'A1B21C'; strlps = '121'  #string中的最长回文子序列
    print(getPalindromel(string))
    # getPalindromel(string)

    string2 = 'A1BC22DE1F'; strlps2 = '1221'
    print(getPalindrome2(string2, strlps2))
