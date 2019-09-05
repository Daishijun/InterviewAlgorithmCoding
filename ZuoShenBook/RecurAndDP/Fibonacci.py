# -*- coding: utf-8 -*-
# @Date    : 2019/6/2
# @Time    : 17:54
# @Author  : Daishijun
# @File    : Fibonacci.py
# Software : PyCharm

'''最主要的是记录矩阵乘方算法'''

def matMulti(mat1, mat2):
    res = [[0 for j in range(len(mat2[0]))] for i in range(len(mat1))]
    for i in range(0, len(mat1)):
        for j in range(0, len(mat2[0])):
            for k in range(0, len(mat2)):
                res[i][j] += mat1[i][k]*mat2[k][j]
    return res

def matPower(mat, power):    #用power的二进制每个位上的1,0表示， 计算平方。
    res = [[0 for j in range(len(mat[0]))] for i in range(len(mat))]
    for i in range(0, len(res)):
        res[i][i] = 1
    tmp = mat[:][:]
    while power:
        if power &1 :
            res = matMulti(res, tmp)
        tmp = matMulti(tmp, tmp)
        power = power>>1
    return res


'''剑指offer的幂次计算'''
def powerWithUnsignedExp(base, exp):
    '''
    实现
    :param base:
    :param exp:
    :return:
    '''
    res = 1
    tmp = base
    while exp:
        if exp & 1 :
            res = tmp * res
        tmp = tmp*tmp
        exp = exp >>1
    return res

if __name__ =='__main__':
    base = 2
    exp = 10
    print(powerWithUnsignedExp(base, exp))
