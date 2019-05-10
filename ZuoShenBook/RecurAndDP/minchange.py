# -*- coding: utf-8 -*-
# @Date    : 2019/4/14
# @Time    : 19:21
# @Author  : Daishijun
# @File    : minchange.py
# Software : PyCharm

#换钱的最少货币数。

def process(arr, ind, rest):    #返回的是使用arr[ind]及以后的货币，来换rest货币所需要的货币张数。
    if ind == len(arr):
        return 0 if rest == 0 else -1    #遍历了所有arr[]的面额之后，如果rest == 0,表示前面的面额已经换完了，则此轮所需张数为0，且标志着一种尝试的成功；-1表示前面的尝试不成功
    res = -1
    k = 0 #使用的货币张数,初始为0，对应着不用这张面额的尝试。
    while k*arr[ind] <=rest:
        nextres = process(arr, ind+1, rest-k*arr[ind])
        if nextres !=-1:    #两种情况，如果==-1，表示后续的尝试失败，如果！=-1，则返回的数值表示使用的最少货币数。在第ind位置的面值的不同张数的循环里，找到从ind到最后的尝试中最少的货币数
            res = nextres+k if res == -1 else min(res, nextres+k)    #res == -1表示第一次进while。而且能通过上面的if证明是有可行尝试的，此时找到一个基准尝试，把res更新为基准；后续维持最小值。
        k+=1
    return res

def minCoins1(arr, aim):
    if not arr or aim <0:
        return -1
    return process(arr, 0, aim)

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

if __name__ == '__main__':
    arr = [5,2,3]; aim = 20
    print(minCoins1(arr,aim))
    print(minCoins_dp(arr,aim))