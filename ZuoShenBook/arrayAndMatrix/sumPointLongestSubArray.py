# -*- coding: utf-8 -*-
# @Date    : 2019/5/15
# @Time    : 18:17
# @Author  : Daishijun
# @File    : sumPointLongestSubArray.py
# Software : PyCharm

'''
未排序数组中累加和为给定值的最长子数组系列问题
元素可正，可负，可0
'''

def maxLength(arr, k):
    if not arr:
        return 0
    mapdict = {}
    mapdict[0] = -1
    maxlen  = 0
    ssum  = 0
    for i in range(len(arr)):
        ssum += arr[i]
        if ssum - k in mapdict.keys():
            maxlen = max(maxlen, i - mapdict[ssum - k])
        if ssum not in mapdict.keys():
            mapdict[ssum] = i
    return maxlen

if __name__ == '__main__':
    arr = [1,2,3,3]
    k = 6
    print(maxLength(arr, k))
