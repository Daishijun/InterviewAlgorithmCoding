# -*- coding: utf-8 -*-
# @Date    : 2019/4/30
# @Time    : 16:17
# @Author  : Daishijun
# @File    : squareRotate.py
# Software : PyCharm

'''
正方形矩阵顺时针转动90°,  一圈一圈旋转
'''

def rotateEdge(mat, startR, startC, endR, endC):
    times = endR - startR
    tmp = 0
    for i in range(0, times):
        tmp = mat[startR][startC+i]
        mat[startR][startC + i] = mat[endR-i][startC]
        mat[endR - i][startC] = mat[endR][endC-i]
        mat[endR][endC - i] = mat[startR+i][endC]
        mat[startR + i][endC] = tmp


def rotate(mat):
    startR , startC = 0, 0
    endR , endC = len(mat)-1, len(mat[0])-1
    while startR<endR:
        rotateEdge(mat, startR, startC, endR, endC)
        startR +=1; startC+=1
        endR -=1; endC -=1

if __name__ == '__main__':
    mat = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]
    rotate(mat)
    print(mat)