#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/29 22:48
# @Author   : Daishijun
# @Site     : 
# @File     : maxBoundingOneSquare.py
# @Software : PyCharm

'''Leetcode 1139 最大的以1为边界的正方形'''

class Solution:
    def largest1BorderedSquare(self, grid) -> int:
        def setMap(grid):
            rows = len(grid)
            cols = len(grid[0])
            rightmat = [[0]*cols for i in range(rows)]
            downmat = [[0]*cols for i in range(rows)]

            if grid[-1][-1] == 1:
                rightmat[rows-1][cols-1] =1
                downmat[rows-1][cols-1] = 1
            for i in range(rows-2, -1, -1):
                if grid[i][-1] == 1:
                    rightmat[i][cols-1] = 1
                    downmat[i][cols-1] = downmat[i+1][cols-1] +1
            for j in range(cols-2, -1, -1):
                if grid[-1][j] ==1:
                    rightmat[rows-1][j] = rightmat[rows-1][j+1]+1
                    downmat[rows-1][j] = 1
            for i in range(rows-2, -1, -1):
                for j in range(cols-2, -1, -1):
                    if grid[i][j] == 1:
                        rightmat[i][j] = rightmat[i][j+1]+1
                        downmat[i][j] = downmat[i+1][j] +1
            return rightmat, downmat

        rmat, dmat = setMap(grid)

        def hasSizeBoard(size, rmat, dmat):
            for i in range(len(rmat)-size+1):
                for j in range(len(rmat[0])-size+1):
                    if rmat[i][j]>=size and dmat[i][j] >=size \
                        and rmat[i+size-1][j]>=size and dmat[i][j+size-1]>=size:
                        return True
            return False

        for size in range(min([len(grid), len(grid[0])]), 0, -1):
            if hasSizeBoard(size, rmat, dmat):
                return size**2
        return 0

