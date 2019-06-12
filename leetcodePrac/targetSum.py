# -*- coding: utf-8 -*-
# @Date    : 2019/6/5
# @Time    : 14:31
# @Author  : Daishijun
# @File    : targetSum.py
# Software : PyCharm

'''Leetcode 494 目标和'''

def targetsum(nums, target):
    if not nums:
        return 0
    return process(nums, 0, target)

def process(nums, index, rest):
    if index == len(nums):
        return 1 if rest == 0 else 0
    return process(nums, index+1, rest-nums[index]) + process(nums, index+1, rest+nums[index])

def targetsum2(nums, target):
    if not nums:
        return 0
    totalsum = sum(nums)
    if totalsum < target or -totalsum > target:
        return 0
    dp = [[0 for i in range(2*totalsum+1)] for j in range(len(nums)+1)]
    dp[len(nums)][totalsum-target] = 1    #初始位置和目标位置的设置是坑！！！
    for i in range(len(nums)-1, -1, -1):
        for j in range(len(dp[0])):
            if j-nums[i] >-1 :
                dp[i][j] += dp[i+1][j-nums[i]]
            if j+nums[i] < len(dp[0]):
                dp[i][j] += dp[i+1][j+nums[i]]
    for line in dp:
        print(line)
    return dp[0][totalsum]

def targetsum3(nums, target):
    if not nums:
        return 0
    totalsum = sum(nums)
    if totalsum < target or -totalsum > target:
        return 0
    dp = [[0 for i in range(2*totalsum+1)] for j in range(2)]
    dp[1][totalsum-target] = 1    #初始位置和目标位置的设置是坑！！！
    r1 = 0; r2 = 1
    for i in range(len(nums)-1, -1, -1):
        for j in range(len(dp[0])):
            if j-nums[i] >-1 :
                dp[r1][j] += dp[r2][j-nums[i]]
            if j+nums[i] < len(dp[0]):
                dp[r1][j] += dp[r2][j+nums[i]]
        r1, r2 = r2, r1
        dp[r1] = [0]*len(dp[r2])
    for line in dp:
        print(line)
    return dp[r2][totalsum]

'''!!!神奇了！！！'''
def targetsum4(nums, target):
    if not nums:
        return 0
    totalsum = sum(nums)
    if totalsum < target or -totalsum > target:
        return 0
    if (target+totalsum) & 1 :
        return 0
    tmp = (target+totalsum)>>1
    #目标就是从nums中找到组成累加和为tmp的集合
    dp = [0 for i in range(tmp+1)]     #用了空间压缩解决这个01dp问题，dp[i][j] ==>用[0,i]位置的数字组成tmp的方法数
    dp[0] =1 #累加和为0时初始就有一种情况
    for ind in range(len(nums)):
        for i in range(tmp, nums[ind]-1, -1):
            dp[i] += dp[i-nums[ind]]
    return dp[-1]




if __name__ == '__main__':
    nums = [1,1,1,1,1]
    target = 3
    print(targetsum(nums, target))
    print(targetsum3(nums, target))
    print(targetsum4(nums, target))