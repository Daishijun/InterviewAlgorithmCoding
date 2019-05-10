# -*- coding: utf-8 -*-
# @Date    : 2019/5/5
# @Time    : 16:51
# @Author  : Daishijun
# @File    : needSortMinLenSubarray.py
# Software : PyCharm

'''
需要排序的最短子数组长度
'''
'''
两个方向遍历数组，记录下需要变换的临界位置。
'''

def getMinLength(arr):
    if not arr or len(arr)<2:
        return 0
    minvalue = arr[-1]
    noMinindex = -1
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > minvalue:
            noMinindex = i
        else:
            minvalue = min(minvalue, arr[i])
    if noMinindex == -1:
        return 0
    maxvalue = arr[0]
    noMaxindex = -1
    for j in range(1, len(arr)):
        if arr[j] < maxvalue:
            noMaxindex = j
        else:
            maxvalue = max(maxvalue, arr[j])
    print('noMaxindex:', noMaxindex)
    print('noMinindex:', noMinindex)
    return noMaxindex - noMinindex +1

if __name__ == '__main__':
    arr = [1, 5, 3, 4, 2, 6, 7]
    print(getMinLength(arr))