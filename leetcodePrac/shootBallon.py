# -*- coding: utf-8 -*-
# @Date    : 2019/6/8
# @Time    : 21:22
# @Author  : Daishijun
# @File    : shootBallon.py
# Software : PyCharm

'''Leetcode 312  戳气球'''

def macCoins(nums):
    arr = [0 for i in range(len(nums)+2)]
    arr[0] = 1
    arr[-1] = 1
    for i in range(len(nums)):
        arr[i+1] = nums[i]
    return process(arr, 1, len(nums))

def process(arr, left, right):
    if left == right :
        return arr[left-1] * arr[left]* arr[right+1]
    maxval = max(arr[left-1]* arr[left] * arr[right+1]+process(arr, left+1, right), arr[right+1]*arr[right]*arr[left-1]+process(arr, left, right-1))
    for i in range(left+1, right):
        maxval = max(maxval, process(arr, left, i-1)+ arr[left-1]* arr[i]* arr[right+1]+process(arr, i+1, right))
    return maxval

def maxCoinsDp(nums):
    if not nums:
        return 0
    if len(nums)==1:
        return nums[0]
    arr = [1] + nums+ [1]
    dp = [[0 for i in range(len(arr))] for j in range(len(arr))]
    for i in range(1, len(nums)+1):
        dp[i][i] = arr[i-1] * arr[i] * arr[i+1]
    for i in range(len(nums), 0, -1):
        for j in range(i, len(nums)+1):
            dp[i][j] = max(arr[i-1]*arr[i]*arr[j+1]+ dp[i+1][j], arr[j+1]*arr[j]*arr[i-1]+ dp[i][j-1])
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k-1]+arr[i-1]*arr[k]*arr[j+1]+dp[k+1][j])
    return dp[1][len(nums)]



if __name__ == '__main__':
    nums = [3,1,5,8]
    print(macCoins(nums))
    print(maxCoinsDp(nums))

