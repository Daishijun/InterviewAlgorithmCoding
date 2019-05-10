# -*- coding: utf-8 -*-
# @Date    : 2019/5/6
# @Time    : 23:05
# @Author  : Daishijun
# @File    : subMatrixSum.py
# Software : PyCharm

'''
子矩阵的最大累加和问题
'''

def maxSum(mat):
    if not mat or len(mat)==0 or len(mat[0])==0:
        return 0
    mmax = -float('inf')
    cur = 0
    sumlist = [0 for i in range(len(mat[0]))]    #累加矩阵，即第i行到第j行的各列的累加和
    for i in range(len(mat)):    #从第i行开始的子矩阵
        for j in range(i, len(mat)):    #首先是只包含第i行一行的子矩阵，然后依次向下累积每一行矩阵
            cur = 0
            for k in range(len(mat[0])):
                sumlist[k] +=mat[j][k]
                cur += sumlist[k]
                mmax = max(mmax, cur)
                if cur <0:
                    cur = 0
                else:
                    cur = cur
    return mmax

if __name__ == '__main__':
    mat = [[-1, -1, -1],[-1, 2, 2],[-1, -1, -1]]
    print(maxSum(mat))


