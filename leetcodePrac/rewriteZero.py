#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/16 10:33
# @Author   : Daishijun
# @Site     : 
# @File     : rewriteZero.py
# @Software : PyCharm

'''LeetCode 141 周赛1 复写0'''

'''
这里想复杂了，实现了一个空间复杂度O(1)的原地算法。
'''

class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        flag = 0
        count  = 0
        for ind in range(len(arr)) :

            if arr[ind] == 0:
                count +=1
            if count + ind >= len(arr) - 1:
                if arr[ind] == 0 and count + ind > len(arr)-1:
                    flag = 1
                break
        back = len(arr)-1
        print('ind', ind)
        print('flag', flag)
        arr[back] = arr[ind]
        if arr[ind] == 0 and not flag:
            back -=1
            arr[back] = arr[ind]
        back-=1
        ind -=1
        for j in range(ind, -1, -1):
            arr[back] = arr[j]
            if arr[j] == 0 :

                back -=1
                arr[back] = 0
            back -=1
            print('back:',back, 'j:',j)

if __name__ == '__main__':
    # arr = [1,5,2,0,6,8,0,6,0]
    # arr = [8,5,0,9,0,3,4,7]
    arr = [8,4,5,0,0,0,0,7]
    S = Solution()
    S.duplicateZeros(arr)
    print(arr)