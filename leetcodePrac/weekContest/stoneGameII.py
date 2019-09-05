#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/30 20:13
# @Author   : Daishijun
# @Site     : 
# @File     : stoneGameII.py
# @Software : PyCharm

'''石子游戏 II'''

class Solution:
    def stoneGameII(self, piles) -> int:
        dictf = {}
        dicts = {}
        def helpf(M, start):
            if len(piles)-start<=2*M:
                dictf[(M, start)] = sum(piles[start:])
                return dictf[(M, start)]
            res = 0
            for i in range(1, 2*M+1):
                if (max(M, i), start+i) not in dicts.keys():
                    dicts[(max(M, i), start+i)] = helps(max(M, i), start+i)
                res = max(res, sum(piles[start:start+i])+dicts[(max(M, i), start+i)])
            dictf[(M, start)] = res
            return res
        def helps(M, start):
            if len(piles)-start<=2*M:
                dicts[(M, start)] = 0
                return dicts[(M, start)]
            res = float('inf')
            for i in range(1, 2*M+1):
                if (max(M, i), start+i) not in dictf.keys():
                    dictf[max(M, i), start+i] = helpf(max(M,i), start+i)
                res = min(res, dictf[max(M, i), start+i])
            dicts[(M, start)] = res
            return res
        return helpf(1, 0)

    def stoneGameIII(self, piles) -> int:

        def helpf(M, start):
            if len(piles)-start<=2*M:

                return sum(piles[start:])


            return max([sum(piles[start:start+i])+helps(max(M, i), start+i) \
                        for i in range(1, 2*M+1)])
        def helps(M, start):
            if len(piles)-start<=2*M:

                return 0


            return min(helpf(max(M,i), start+i) for i in range(1, 2*M+1))
        return helpf(1, 0)


    # def stoneGameII(self, piles) -> int:
    #     fmat = [[0]*len(piles[0]) for i in range(len(piles))]
    #     smat = [[0]*len(piles[0]) for i in range(len(piles))]
    #     for

if __name__ == '__main__':
    S = Solution()
    # piles = [2,7,9,4,4]
    piles = [9,2,2,8,3,7,9,9]
    print(S.stoneGameII(piles))