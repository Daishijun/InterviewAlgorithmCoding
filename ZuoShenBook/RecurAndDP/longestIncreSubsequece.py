# -*- coding: utf-8 -*-
# @Date    : 2019/4/15
# @Time    : 20:36
# @Author  : Daishijun
# @File    : longestIncreSubsequece.py
# Software : PyCharm

'''求数组的最长递增子序列'''
def getdp1(arr):
    dp = [1 for i in range(len(arr))]
    for i in range(len(dp)):
        for j in range(0, i):
            if arr[j]<arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp



def generateList(arr, dp):
    length = max(dp)
    endind = dp.index(length)
    res = [arr[endind]]
    for ind in range(endind-1, -1, -1):
        if arr[ind]<arr[endind] and dp[ind] == dp[endind]-1:
            res.insert(0, arr[ind])
            endind = ind
    return res

def lis1(arr):
    if not arr :
        return None
    dp = getdp1(arr)

    return generateList(arr,dp)

def getdp2(arr):    #用二分法来优化生成dp的时间
    dp = [1 for i in range(len(arr))]
    ends = [0 for i in range(len(arr))]
    ends[0] = arr[0]
    right = 0
    l = 0
    r = 0
    m = 0
    for i in range(1, len(arr)):
        l = 0
        r = right
        while l<=r:
            m = (l+r)>>1
            if arr[i] > ends[m]:
                l = m+1
            else:     #这里包括相等的情况，即相等时把右边界左移，左边界不变，直到右边界<左边界。
                r = m-1
        right = max(l, right)
        ends[l] = arr[i]    #更新有效区内每个长度（用下标表示）的最小结尾数。
        dp[i] = l+1
    return dp

def lis2(arr):    #调用二分法生成dp
    if not arr:
        return None
    dp = getdp2(arr)

    return generateList(arr, dp)

if __name__ == '__main__':
    arr = [2,1,5,3,6,4,8,9,7]
    print(lis1(arr))
    print(lis2(arr))


