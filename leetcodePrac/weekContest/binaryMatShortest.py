#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/16 11:39
# @Author   : Daishijun
# @Site     : 
# @File     : binaryMatShortest.py
# @Software : PyCharm

'''Leetcode 141周赛 第三题，二进制矩阵中的最短路径'''
'''
宽度优先遍历，每深入一层，path +=1 ；当遇到最后的点的时候返回path，遍历都没找到path就返回-1

这里学到了用两个queue交替来实现宽度优先遍历（对应树的层次遍历）
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        if not grid or grid == [] or grid[0] == []:
            return -1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        stack = [[0,0]]
        res = 1
        dx = [-1,-1, 1, 1, 0, 0, 1,-1]
        dy = [-1, 1, 1,-1,-1, 1, 0, 0]
        visited = [[0]*cols for i in range(rows)]

        while stack:
            nextstack = []
            for [row, col] in stack:
                for i in range(8):
                    newx = row +dx[i]
                    newy = col +dy[i]
                    if newx<0 or newx>=rows or newy<0 or newy>=cols or grid[newx][newy] or visited[newx][newy]:
                        continue
                    if newx == rows-1 and newy == cols-1 :
                        return res+1
                    else:
                        nextstack.append([newx, newy])
                        visited[newx][newy] = 1
            stack = nextstack    #到下一层
            res +=1
        return -1



if __name__ =='__main__':
    S = Solution()
    mat = [[0,0,1,1,0,0],[0,0,0,0,1,1],[1,0,1,1,0,0],[0,0,1,1,0,0],[0,0,0,0,0,0],[0,0,1,0,0,0]]
    print(S.shortestPathBinaryMatrix(mat))

