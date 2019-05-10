# -*- coding: utf-8 -*-
# @Date    : 2019/4/2
# @Time    : 20:22
# @Author  : Daishijun
# @File    : prac1.py
# Software : PyCharm

import sys

#一行内输入两个数字，用空格分隔
# n, m = map(int, sys.stdin.readline().strip().split())
# print(type(n))
# print('n', n)
# print('m', m)


#输入一行数组，以空格分隔
# a, b = map(int,input('values:').split())
# print(type(a))
# print(a)

#输入m行数据，作为一个二维数组
m, n = map(int,input('values:').split())
matrix = []
for i in range(m):
    rlist = list(map(int, input().split()))
    matrix.append(rlist)

print(matrix)
