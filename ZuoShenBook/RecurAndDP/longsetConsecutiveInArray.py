# -*- coding: utf-8 -*-
# @Date    : 2019/4/20
# @Time    : 13:55
# @Author  : Daishijun
# @File    : longsetConsecutiveInArray.py
# Software : PyCharm

'''
数组中的最长连续序列
'''

def merge(mapdict, less, more):
    left = less - mapdict[less]+1
    right = more + mapdict[more] -1
    length = right-left +1
    mapdict[left] = length
    mapdict[right] = length

    return length

def longestConsecutive(arr):
    if not arr:
        return 0
    maxlen =1
    mapdict = {}
    for i in range(len(arr)):
        if arr[i] not in mapdict.keys():
            mapdict[arr[i]] = 1
            if arr[i] -1 in mapdict.keys():
                maxlen = max(maxlen, merge(mapdict, arr[i]-1, arr[i]))
            if arr[i] +1 in mapdict.keys():
                maxlen = max(maxlen, merge(mapdict, arr[i], arr[i]+1))

    return maxlen

if __name__ == '__main__':
    arr = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(arr))

    str1 = 'abcdabccd'
    str2 = 'bcq'
    print(str1.count(str2))