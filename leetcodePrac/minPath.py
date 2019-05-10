# -*- coding: utf-8 -*-
# @Date    : 2019/4/15
# @Time    : 20:57
# @Author  : Daishijun
# @File    : minPath.py
# Software : PyCharm
'''
leetcode 64 最小路径和
'''


class Solution:
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dp = grid[0].copy()
        for j in range(1, cols):
            dp[j] += dp[j-1]
        for row in range(1, rows):
            for col in range(0, cols):
                if col == 0:
                    dp[col] += grid[row][col]
                else:
                    dp[col] = min(dp[col], dp[col-1]) + grid[row][col]
        return dp[cols-1]

if __name__=='__main__':
    # grid = [[1,3,1],[1,5,1],[4,2,1]]
    # ss = Solution()
    # print(ss.minPathSum(grid))
    num = 0
    print(sum(map(int,list(bin(num)[2:]))))

