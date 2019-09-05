#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/4 20:55
# @Author   : Daishijun
# @Site     : 
# @File     : LongestChunkedPalindromeDecomposition.py
# @Software : PyCharm

'''5150 段式回文'''

class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 0
        l = 0
        r = len(text)
        ind = 1
        while l<r:
            if  l+ind >r-ind:
                res +=1
                # print('larger ')
                break

            elif text[l:l+ind] == text[r-ind:r]:
                res +=2
                l += ind
                r -= ind
                ind = 1
                # print('equal')
                # print('l:', l, 'r:',r)
            else :
                ind +=1
        return res

if __name__ == '__main__':
    S = Solution()
    text = "aaa"
    print(S.longestDecomposition(text))
