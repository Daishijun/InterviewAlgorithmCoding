#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/21 11:04
# @Author   : Daishijun
# @Site     : 
# @File     : prob3.py
# @Software : PyCharm

class Solution:
    def __init__(self):
        self.res = 0
    def mctFromLeafValues(self, arr) -> int:

        self.helper(arr)
        return self.res

    def helper(self, arr):
        print('res:', self.res)
        if len(arr) <2:
            return arr[0]
        if len(arr) <3:
            self.res += arr[0]*arr[1]
            return max(arr)

        maxind = arr.index(max(arr))
        print('ind:',maxind)
        if maxind == 0:
            left = 0
        else:
            left = self.helper(arr[:maxind])
        if maxind == len(arr)-1:
            right = 0
        else:
            right = self.helper(arr[maxind+1:])
        self.res += arr[maxind]*max(left, right)
        print('res:', self.res, 'max:',arr[maxind])
        return arr[maxind]

class Solution:
    def __init__(self):
        self.res = 0

    def mctFromLeafValues(self, arr) -> int:
        while len(arr)>1:
            left = arr[0]*max(arr[1:])
            right = arr[-1]*max(arr[:-1])
            if left>right:
                arr.pop(-1)
                self.res += right
            else:
                arr.pop(0)
                self.res +=left
        return self.res


if __name__ == '__main__':
    S= Solution()
    # arr = [6,2,4]
    arr = [15,13,5,3,15]
    # arr = [11,12,12]
    print(S.mctFromLeafValues(arr))


