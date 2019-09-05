# -*- coding: utf-8 -*-
# @Date    : 2019/6/5
# @Time    : 14:31
# @Author  : Daishijun
# @File    : targetSum.py
# Software : PyCharm

'''Leetcode 494 目标和'''

def targetsum(nums, target):    #递归回溯
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
    dp = [[0 for i in range(2*totalsum+1)] for j in range(len(nums)+1)]    #j列应该是指当前剩余和为j的方法数； 、
                            # i行表示当前考虑第i个数字，用第i个到最后一个数字组成剩余的j
    dp[len(nums)][totalsum] = 1    #初始位置和目标位置的设置是坑！！！   对应的是最后应该剩余0，==》对应的就是totalsum
    for i in range(len(nums)-1, -1, -1):
        for j in range(len(dp[0])):    #遍历每个sum和的数值，
            if j-nums[i] >-1 :
                dp[i][j] += dp[i+1][j-nums[i]]
            if j+nums[i] < len(dp[0]):
                dp[i][j] += dp[i+1][j+nums[i]]
    for line in dp:
        print(line)
    return dp[0][totalsum+target]    #第【0，len(nums)-1】个数字，剩余target

def targetsum3(nums, target):    #这里是从左往右进行计算，和上边的不一样，到最后应该是剩余0，初始剩余target。
    if not nums:
        return 0
    totalsum = sum(nums)
    if totalsum < target or -totalsum > target:
        return 0
    dp = [[0 for i in range(2*totalsum+1)] for j in range(2)]
    dp[1][totalsum+target] = 1    #初始位置和目标位置的设置是坑！！！  这块还是得斟酌一下，好像应该是+
    r1 = 0; r2 = 1
    # for i in range(len(nums)-1, -1, -1):
    for i in range(0, len(nums)):
        for j in range(len(dp[0])):
            if j-nums[i] >-1 :
                dp[r1][j] += dp[r2][j-nums[i]]
            if j+nums[i] < len(dp[0]):
                dp[r1][j] += dp[r2][j+nums[i]]
        r1, r2 = r2, r1
        dp[r1] = [0]*len(dp[r2])
    for line in dp:
        print(line)
    return dp[r2][totalsum]    #到最后一个位置，剩余0

'''!!!神奇了！！！'''
def targetsum4(nums, target):
    if not nums:
        return 0
    totalsum = sum(nums)
    if totalsum < target or -totalsum > target:
        return 0
    if (target+totalsum) & 1 :    #很巧，如果A+B= totalSum，A-B= target；那么两者相加等于2A，肯定是个偶数。
        return 0
    tmp = (target+totalsum)>>1    #这个就是2A//2 == >A ,即前面挂正号的数字和。
    #目标就是从nums中找到组成累加和为tmp的集合
    dp = [0 for i in range(tmp+1)]     #用了空间压缩解决这个01dp问题，dp[i][j] ==>用[0,i]位置的数字组成tmp的方法数
    dp[0] =1 #累加和为0时初始就有一种情况
    for ind in range(len(nums)):    #从nums[0]开始考虑是否放入背包
        for i in range(tmp, nums[ind]-1, -1):    #这里的终止位置设为nums[ind]，是为了保证i-nums[ind]>=0,如果小于0的话，直接dp[i] = dp[i]就行了
            dp[i] = dp[i] + dp[i-nums[ind]]  #就是取不取这个num[ind]
    return dp[-1]    #最后累加和为tmp



def targetsum22(nums, target):    #正向的，dp[i][j]表示使用【0，i】个数字，组成和为j的方法数。
    if not nums:
        return 0
    totalsum = sum(nums)
    if totalsum < target or -totalsum > target:
        return 0
    dp = [[0 for i in range(2*totalsum+1)] for j in range(len(nums))]    #j列应该是指当前和为j的方法数； i行表示使用【i,end】个数字
    dp[0][nums[0]+totalsum] = 1    #初始位置和目标位置的设置是坑！！！
    dp[0][totalsum-nums[0]] = 1    #初始位置和目标位置的设置是坑！！！
    for i in range(1, len(nums)):
        for j in range(len(dp[0])):    #遍历每个sum和的数值，
            if j-nums[i] >-1 :
                dp[i][j] += dp[i-1][j-nums[i]]
            if j+nums[i] < len(dp[0]):
                dp[i][j] += dp[i-1][j+nums[i]]
    for line in dp:
        print(line)
    return dp[len(nums)-1][totalsum+target]    #第【0，len(nums)-1】个数字，剩余target == 0


if __name__ == '__main__':
    nums = [1,1,1,1,1]
    target = 3
    # print(targetsum(nums, target))
    print(targetsum2(nums, target))
    print(targetsum3(nums, target))
    # print(targetsum4(nums, target))
