# -*- coding: utf-8 -*-
# @Date    : 2019/4/15
# @Time    : 19:03
# @Author  : Daishijun
# @File    : shootballon.py
# Software : PyCharm

def process(arr, L, R):
    if L == R:
        return arr[L-1]*arr[L]*arr[R+1]
    maxval = max(arr[L-1]*arr[L]*arr[R+1]+process(arr, L+1, R), arr[L-1]*arr[R]*arr[R+1]+process(arr,L, R-1))
    for i in range(L+1,R):
        maxval = max(maxval, arr[L-1]*arr[i]*arr[R+1]+process(arr,L,i-1)+process(arr,i+1,R))
    return maxval

def maxScore1(arr):

    if not arr :
        return 0
    if len(arr)==1:
        return arr[0]
    N = len(arr)
    helparr = [1]+arr+[1]
    return process(helparr, 1, N)

def maxScore2_dp(arr):
    if not arr:
        return 0
    if len(arr)==1:
        return arr[0]
    N = len(arr)
    helparr = [1]+arr+[1]
    dp = [[0 for i in range(len(helparr))] for j in range(len(helparr))]
    for i in range(1,N+1):
        dp[i][i] = helparr[i-1]*helparr[i]*helparr[i+1]
    for L in range(N,0,-1):
        for R in range(L,N+1):
            finalL = helparr[L-1]*helparr[L]*helparr[R+1]+ dp[L+1][R]
            finalR = helparr[L-1]*helparr[R]*helparr[R+1] + dp[L][R-1]
            dp[L][R] = max(finalL, finalR)
            for i in range(L+1, R):
                dp[L][R] = max(dp[L][R], helparr[L-1]*helparr[i]*helparr[R+1]+dp[L][i-1]+dp[i+1][R])
    return dp[1][N]

if __name__ == '__main__':
    arr =[3,2,5]
    print(maxScore1(arr))
    print(maxScore2_dp(arr))