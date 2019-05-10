# -*- coding: utf-8 -*-
# @Date    : 2019/4/29
# @Time    : 19:31
# @Author  : Daishijun
# @File    : xorSumSplit.py
# Software : PyCharm

'''
子数组异或和为0的最多划分
'''

#dp[i] ==> 在arr[0...i]上做分割，异或和为0的子数组最多多少个

def mostEOR(arr):
    if not arr or len(arr)==0:
        return 0
    # eor = 0    ==>这里应该是左神出错了，这里初值赋值为0没问题，但是后续for循环从1开始，arr[0]的值没有异或到eor中。
    dp = [0 for i in range(len(arr))]
    mapdict = {}
    mapdict[0] = -1
    dp[0] = 1 if arr[0]==0 else 0
    mapdict[arr[0]] = 0
    eor = arr[0]    #==》修正，把arr[0]的值异或进eor中。
    for i in range(1, len(arr)):
        eor ^=arr[i]
        if eor in mapdict.keys():
            preEorIndex = mapdict[eor]
            dp[i] = 1 if preEorIndex==-1 else dp[preEorIndex]+1
        dp[i] = max(dp[i-1], dp[i])
        mapdict[eor] = i
    print(eor)
    return dp[-1]

if __name__ == '__main__':
    # arr = [3,2,1,9,0,7,0,2,1,3]
    arr = [6,3,2,1]
    print(mostEOR(arr))