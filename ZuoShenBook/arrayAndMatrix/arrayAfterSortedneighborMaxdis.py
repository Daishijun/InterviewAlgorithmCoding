# -*- coding: utf-8 -*-
# @Date    : 2019/5/20
# @Time    : 16:10
# @Author  : Daishijun
# @File    : arrayAfterSortedneighborMaxdis.py
# Software : PyCharm

'''数组排序之后相邻数的最大差值'''


def maxGap(nums):
    if not nums or len(nums)<2:
        return 0
    length = len(nums)
    minval = min(nums)
    maxval = max(nums)
    if minval == maxval:
        return 0
    hasNum = [False for i in range(length+1)] #N个数字建立N+1个桶， 最大值单独装进一个桶, 必然会有一个空桶，而且最小值肯定装进最小桶，所以空桶一定在中间位置
    maxlist = [0 for i in range(length+1)]
    minlist = [0 for i in range(length+1)] #每个桶的最大值和最小值

    for i in range(length):
        bid = bucket(nums[i], length, maxval, minval)
        minlist[bid] = nums[i] if not hasNum[bid] else min(minlist[bid], nums[i])
        maxlist[bid] = nums[i] if not hasNum[bid] else max(maxlist[bid], nums[i])
        hasNum[bid] = True
    res = 0
    lastMax= maxlist[0]
    for ind in range(1, length+1):
        if hasNum[ind]:
            res = max(res, minlist[ind] - lastMax)
            lastMax = maxlist[ind]
    return res

def bucket(num, length, maxval, minval):
    return (num-minval)*length/(maxval-minval)

if __name__ == '__main__':
    arr = [9 ,3, 1,10]
    print(maxGap(arr))