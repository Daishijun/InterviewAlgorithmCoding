# -*- coding: utf-8 -*-
# @Date    : 2019/5/19
# @Time    : 10:56
# @Author  : Daishijun
# @File    : boundaryOneMaxSquare.py
# Software : PyCharm

'''边界都是1的最大正方形大小'''

'''预处理数组，仍然是O(N3)的复杂度，需要检查每一个点作为正方形的左上角O(N2)，检查边长长度O(N)，检查4条边是否都是1'''

def setBorderMap(mat, rightmat, downmat):    #对两个预处理矩阵进行修改,使用预处理矩阵来加速检查4条边的过程
    rows = len(mat)
    cols = len(mat[0])

    if mat[rows-1][cols-1] == 1:
        rightmat[rows-1][cols-1] = 1
        downmat[rows-1][cols-1] = 1
    for i in range(rows-2, -1, -1):
        if mat[i][cols-1] == 1:
            downmat[i][cols-1] = downmat[i+1][cols-1] +1
            rightmat[i][cols-1] = 1
        else:    #初始化都为0的话，可以不设置
            downmat[i][cols - 1] = 0
            rightmat[i][cols - 1] = 0
    for j in range(cols-2, -1, -1):
        if mat[rows-1][j] ==1:
            rightmat[rows-1][j] = rightmat[rows-1][j+1] + 1
            downmat[rows-1][j] = 1
    for i in range(rows-2, -1, -1):
        for j in range(cols-2, -1, -1):
            if mat[i][j] ==1:
                rightmat[i][j] = rightmat[i][j+1]+1
                downmat[i][j] = downmat[i+1][j]+1

def getMaxSize(mat):
    rightmat = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    downmat = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    setBorderMap(mat, rightmat, downmat)
    for size in range(min(len(mat), len(mat[0])), 0, -1):
        if hasSizeOfBorder(size, rightmat, downmat):
            return size
    return 0


def hasSizeOfBorder(size, rightmat, downmat):
    for i in range(len(rightmat)-size+1):
        for j in range(len(rightmat[0]-size+1)):
            if rightmat[i][j]>=size and downmat[i][j]>=size and downmat[i][j+size-1]>=size and rightmat[i+size-1][j] >=size:
                return True
    return False

