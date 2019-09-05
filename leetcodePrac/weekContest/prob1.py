#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/21 10:41
# @Author   : Daishijun
# @Site     : 
# @File     : prob1.py
# @Software : PyCharm

class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        mapdict = {}
        res = 0
        for li in dominoes:
            li = tuple(li)
            if li in mapdict.keys() or li[::-1] in mapdict.keys():
                if li[0]!=li[1]:
                    res += mapdict.get(li,0) + mapdict.get(li[::-1], 0)
                else:
                    res += mapdict.get(li,0) if li in mapdict.keys() else mapdict.get(li[::-1], 0)
                # print('li:',li)
            mapdict[li] = mapdict.get(li,0)+1

        return res

if __name__ == '__main__':
    S = Solution()
    dom = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    # dom = [[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]
    print(S.numEquivDominoPairs(dom))

