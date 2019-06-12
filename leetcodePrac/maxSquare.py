# -*- coding: utf-8 -*-
# @Date    : 2019/6/5
# @Time    : 17:02
# @Author  : Daishijun
# @File    : maxSquare.py
# Software : PyCharm

'''Leetcode 221 最大正方形'''

'''dp，dp[i][j]记录以i,j位置为右下角的正方形的边长
'''
def maximalSquare(mat):
    if not mat or len(mat) <1 or len(mat[0])<1:
        return 0
    dp = [[0 for j in range(len(mat[0]))] for j in range(len(mat))]
    maxArea = 0
    for i in range(0, len(dp)):
        dp[i][0] = mat[i][0]
        for j in range(0, len(dp[0])):
            if mat[i][j] :
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min([dp[i-1][j-1], dp[i-1][j], dp[i][j-1]]) +1
                maxArea = max(maxArea, pow(dp[i][j], 2))
    return maxArea


'''使用最大矩形的思路，单调栈
'''
def maxSquareArea(map):
    if not map or len(map)<1 or len(map[0])<1:
        return 0
    maxArea = 0
    height = [0 for i in range(len(map[0]))]
    for i in range(len(map)):
        for j in range(len(map[0])):
            height[j] = 0 if map[i][j] == 0 else height[j]+1
        print(height)
        maxArea = max(maxArea, maxSquFromBottom(height))
    return maxArea

def maxSquFromBottom(height):
    if not height or len(height) == 0:
        return 0
    maxArea = 0
    stack = []
    for i in range(len(height)):
        while stack and height[i]<=height[stack[-1]]:
            index = stack.pop()
            left = stack[-1] if stack else -1
            maxArea = max(maxArea, pow(min(height[index],(i-left-1)),2))
        stack.append(i)
    while stack:
        index = stack.pop()
        left = stack[-1] if stack else -1
        maxArea = max(maxArea, pow(min(height[index], (len(height) - left - 1)),2))
    return maxArea



if __name__ == '__main__':
    mat = [[1,0,1,0,0],
           [1,0,1,1,1],
           [1,1,1,1,1],
           [1,0,0,1,0]]
    mat2 = [[1]]
    print(maxSquareArea(mat))
    print(maximalSquare(mat))

