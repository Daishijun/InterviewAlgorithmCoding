# -*- coding: utf-8 -*-
# @Date    : 2019/4/8
# @Time    : 16:11
# @Author  : Daishijun
# @File    : baiduprac1.py
# Software : PyCharm

if __name__ == '__main__':
    N = int(input())
    inlist = []
    for i in range(N):
        inlist.append(list(input().split())[0])

    print('N:', N)
    print('input list:', inlist)
    for i in inlist:
        print(i)