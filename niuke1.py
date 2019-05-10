# -*- coding: utf-8 -*-
# @Date    : 2019/4/3
# @Time    : 16:55
# @Author  : Daishijun
# @File    : niuke1.py
# Software : PyCharm
T = int(input())
inlist = []
for i in range(T):
    N = int(input())
    numlist = list(map(int, input().split()))
    inlist.append([N, numlist])


def getdp(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(n):
        dp[i] = 1
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


def gen(nums, dp):
    maxl = 0
    index = 0
    for i in range(len(nums)):
        if dp[i] > maxl:
            maxl = dp[i]
            index = i
    lis = [0] * maxl
    lis[-1] = nums[index]
    maxl -= 1
    for i in range(index, -1, -1):
        if nums[i] < nums[index] and dp[i] + 1 == dp[index]:
            lis[maxl - 1] = nums[i]
            index = i
            maxl -= 1
    return lis


for [N, nums] in inlist:


    dp = getdp(nums)
    print(gen(nums, dp))
