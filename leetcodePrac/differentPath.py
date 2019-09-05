# -*- coding: utf-8 -*-
# @Date    : 2019/6/2
# @Time    : 20:24
# @Author  : Daishijun
# @File    : differentPath.py
# Software : PyCharm

'''Leetcode 62  不同路径'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j-1] + dp[j]
        return dp[-1]

'''leetcode 63 不同路径II'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        dp = [1 for i in range(len(obstacleGrid[0]))]
        for j in range(0, len(obstacleGrid[0])):
            if obstacleGrid[0][j] == 1:
                dp[j] = 0
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] = dp[j - 1] + dp[j]
        return dp[-1]


'''leetcode 980 不同路径III'''
'''深度优先遍历， 回溯'''

class Solution:
    def uniquePathsIII(self, grid) -> int:
        zorecount = 0
        starti = 0
        startj = 0



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zorecount +=1
                elif grid[i][j] == 1:
                    starti = i
                    startj = j
                elif grid[i][j] == 2:
                    endi = i
                    endj = j
        # print(starti, startj)
        # print(zorecount)


        def dfs(grid, restzero, r, c):
            res = 0
            # print('grid:',grid, 'r:{}, c:{}'.format(r,c), 'rest:{}'.format(restzero))
            if grid[r][c] == 2 and restzero==0:
                return 1
            if grid[r][c] == 2 or restzero==0:
                return 0
            tmp = grid[r][c]
            grid[r][c] = -1

            if r>0 and (grid[r-1][c] in [2, 0]):
                res += dfs(grid, restzero-1, r-1, c)
            if c>0 and (grid[r][c-1] in [2, 0]):
                res += dfs(grid, restzero-1, r, c-1)
            if r < (len(grid)-1) and (grid[r+1][c] in [2, 0]):
                res += dfs(grid, restzero-1, r+1, c)
            if c < (len(grid[0])-1) and (grid[r][c+1] in [2, 0]):
                res += dfs(grid, restzero-1, r, c+1)
            grid[r][c] = tmp
            return res
        res = dfs(grid, zorecount+1, starti, startj)
        return res

'''动态规划'''



if __name__ == '__main__':
    mat = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    so = Solution()
    print(so.uniquePathsIII(mat))