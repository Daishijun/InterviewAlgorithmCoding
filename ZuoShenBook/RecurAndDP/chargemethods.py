# -*- coding: utf-8 -*-
# @Date    : 2019/4/14
# @Time    : 23:39
# @Author  : Daishijun
# @File    : chargemethods.py
# Software : PyCharm

'''
换钱的方法数
'''
def process1(arr, index, aim):
    res = 0
    if index == len(arr):
        res = 1 if aim == 0 else 0
    else:
        k = 0
        while k*arr[index] <=aim:
            res += process1(arr, index+1, aim-k*arr[index])
            k +=1
    return res


def coins1(arr, aim):
    if not arr or aim<0:
        return 0
    return process1(arr, 0 , aim)

#记忆搜索
def process2(arr, index, aim, mapmem):
    if index == len(arr):
        return 1 if aim==0 else 0
    res = 0
    mapval = 0
    k = 0
    while k*arr[index]<=aim:
        mapval = mapmem[index+1][aim - k*arr[index]]
        if mapval == 0:    #未计算过
            res += process2(arr, index+1, aim-k*arr[index], mapmem)
        else:
            if mapval == -1:     #计算过，且返回为0，说明对应的方式不成功。
                res += 0
            else:
                res += mapval
        k+=1
    if res == 0:     #如果该次对应的方法数为0，说明方法行不通
        mapmem[index][aim] = -1
    else:
        mapmem[index][aim] = res
    return res

def coins2(arr, aim):    #加上记忆搜索
    if not arr or aim<0:
        return 0
    mapmem = [[0 for i in range(aim+1)] for j in range(len(arr)+1)]
    return process2(arr, 0, aim, mapmem)

def coins3_dp(arr, aim):
    if not arr or aim<0:
        return 0
    mapdp = [[0 for i in range(aim+1)] for j in range(len(arr))]    #dp[i][j]使用arr[0...i]面额的情况下，组成j的方法数;最后一行表示用全部面额，凑出j的方法数。
    i = 0
    while i*arr[0]<=aim:
        mapdp[0][i*arr[0]] = 1     #只使用第一张钞票，能找回的钱。
        i+=1
    for i in range(len(mapdp)):    #找回0元钱，因为不需要操作，都可以成立，所以都行得通。
        mapdp[i][0] = 1

    for ind in range(1, len(arr)):
        for rest in range(1, aim+1):
            num =0
            k = 0
            while rest-k*arr[ind]>=0:
                num +=mapdp[ind-1][rest-k*arr[ind]]
                k+=1
            mapdp[ind][rest] = num

    return mapdp[-1][aim]    #使用所有面额的钞票。

def coins4_dp(arr, aim):    #书上的根据递推来的，很像背包问题
    if not arr or aim<0:
        return 0
    dp = [[0 for i in range(aim+1)] for j in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0] = 1
    j = 0
    while j*arr[0]<=aim:
        dp[0][j*arr[0]] = 1
        j+=1
    for ind in range(1, len(arr)):
        for rest in range(1, aim+1):
            dp[ind][rest] = dp[ind-1][rest]
            if rest-arr[ind] >=0:
                dp[ind][rest] +=dp[ind][rest-arr[ind]]
    return dp[len(arr)-1][aim]

def coins5_dp_yasuo(arr, aim):
    if not arr or aim<0:
        return 0
    dp = [0 for i in range(aim+1)]
    j = 0
    while j*arr[0] <=aim:
        dp[j*arr[0]] = 1
        j+=1
    for ind in range(1, len(arr)):
        for rest in range(1, aim+1):
            if rest-arr[ind] >=0:
                dp[rest] += dp[rest-arr[ind]]
    return dp[aim]


#这个才是根据一开始的尝试思路改出来的动态规划
def coins6_try(arr, aim):
    if not arr or aim<0:
        return 0
    dp = [[0 for i in range(aim+1)] for j in range(len(arr)+1)]    #dp[i][j]表示，使用arr[i...N-1]的面额凑出j的方法数。（这与前面的dp意义相反）
    dp[len(arr)][0] = 1     #base case为考虑完所有面额后，rest ==0 的时候有一种方式，这其实是表示，当aim==0时，不需要找钱，存在一种方式。而向上一层到dp[len(arr)-1][...]表示在仅使用最后一个面额能够解决的剩余钱数的情况。
    for ind in range(len(arr)-1, -1, -1):
        for rest in range(1, aim+1):
            num = 0
            k = 0
            while k*arr[ind] <=aim:
                num+=dp[ind+1][aim- k*arr[ind]]
                k+=1
            dp[ind][rest] = num
    return dp[0][aim]

def coins6_yasuo(arr, aim):
    if not arr or aim<=0:
        return 0
    dp = [0 for i in range(aim+1)]
    dp[0] = 1
    for ind in range(len(arr)-1, -1, -1):
        for rest in range(1, aim+1):
            if rest-arr[ind]>=0:
                dp[rest] +=dp[rest-arr[ind]]
    return dp[aim]


if __name__ =='__main__':
    arr = [5, 10, 25, 1]
    aim = 15
    print(coins1(arr, aim))
    print(coins2(arr, aim))
    print(coins3_dp(arr, aim))
    print(coins4_dp(arr, aim))
    print(coins5_dp_yasuo(arr, aim))
    print(coins6_try(arr,aim))
    print(coins6_yasuo(arr, aim))


