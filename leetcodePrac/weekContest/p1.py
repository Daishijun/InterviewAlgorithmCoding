#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/1 10:33
# @Author   : Daishijun
# @Site     : 
# @File     : p1.py
# @Software : PyCharm

# class Solution:
#     def numPrimeArrangements(self, n: int) -> int:
#         count = 1
#         if n<2:
#             return n
#         for j in range(3,n+1, 2):
#             i = 2
#             while i**2<=n:
#                 if j%i == 0:
#                     break
#                 else:
#                     i+=1
#             if i**2>n:
#                 count +=1
#                 print(j)
#         print('count:', count)
#         res = 1
#         for i in range(1,count+1):
#             res = res * i
#         for j in range(1, n-count+1):
#             res = res * j
#         return res%(10**9+7)

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        count = 1
        if n<2:
            return n
        numlist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

        for i in range(len(numlist)):
            if numlist[i] > n:
                count = i
                break
        if n>=97:
            count = len(numlist)
        res = 1
        for i in range(1,count+1):
            res = res * i
        for j in range(1,n-count+1):
            res = res * j

        return res%(10**9+7)

if __name__ == '__main__':
    n = 100
    S = Solution()
    print(S.numPrimeArrangements(n))
