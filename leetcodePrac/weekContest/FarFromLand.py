#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/18 11:03
# @Author   : Daishijun
# @Site     : 
# @File     :
# @Software : PyCharm

'''5053 地图分析'''


class Solution:
    def maxDistance(self, grid) -> int:
        n = len(grid)
        queue = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
        det = [[1,0],[-1,0],[0,-1],[0,1]]
        res = -1
        if len(queue) == 0 or len(queue)==n**2:
            return -1

        while queue:
            level_len = len(queue)

            while level_len:
                ox, oy = queue.pop(0)
                level_len -=1
                for dx,dy in det:
                    nx, ny = ox+dx, oy+dy
                    if nx>=0 and nx<n and ny>=0 and ny<n and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        queue.append((nx,ny))
            res +=1
        return res

