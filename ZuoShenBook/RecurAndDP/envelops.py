# -*- coding: utf-8 -*-
# @Date    : 2019/4/16
# @Time    : 17:26
# @Author  : Daishijun
# @File    : envelops.py
# Software : PyCharm

class Envelopes():
    def __init__(self, length, width):
        self.length = length
        self.width = width

def maxEnvelopes(arr):
    ends = [0 for i in range(len(arr))]
    ends[0] = arr[0]
    l = 0
    r = 0
    m = 0
    right = 0
    for i in range(1, len(arr)):
        l = 0
        r = right
        while l<=r:
            m = (l+r)>>1
            if arr[i] > ends[m]:
                l = m+1
            else:
                r = m-1
        right = max(l, right)
        ends[l] = arr[i]
    return right+1


if __name__ == '__main__':
    lis = [[3,4],[2,3],[4,5],[1,3],[2,2],[3,6],[1,2],[3,2],[2,4]]
    lis.sort(key=lambda x:(x[0], -x[1]))
    print(lis)
    widlist = [x[1] for x in lis]
    print(widlist)
    print(maxEnvelopes(widlist))