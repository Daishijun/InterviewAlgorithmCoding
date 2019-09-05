#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/3 20:22
# @Author   : Daishijun
# @Site     : 
# @File     : prob3.py
# @Software : PyCharm

N = int(input())
tolist = [[0] * 2 for i in range(N)]
for i in range(N):
    tolist[i][0], tolist[i][1] = list(map(int, input().split()))

def getres(arr):
    ends = [0 for i in range(len(arr))]
    ends[0] = arr[0]
    left = 0
    right = 0
    m = 0
    right = 0
    for i in range(1, len(arr)):
        left = 0
        right = right
        while left<=right:
            m = (left+right)>>1
            if arr[i] >= ends[m]:
                left = m+1
            else:
                right = m-1
        right = max(left, right)
        ends[left] = arr[i]
    return right+1

tolist.sort(key=lambda x:(x[0], -x[1]))
wlist = [x[1] for x in tolist]
print(getres(wlist))