# -*- coding: utf-8 -*-
# @Date    : 2019/4/3
# @Time    : 20:14
# @Author  : Daishijun
# @File    : bag1.py
# Software : PyCharm

def bag(n ,c, wlist, vlist):
    # wlist = [2,2,3,5,1]
    # vlist = [5,4,3,5,2]
    valuel = [[0 for j in range(c+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, c+1):
            valuel[i][j] = valuel[i-1][j]
            if j>=wlist[i-1] and valuel[i][j] < valuel[i-1][j-wlist[i-1]]+vlist[i-1]:
                valuel[i][j] = valuel[i-1][j-wlist[i-1]]+vlist[i-1]

    return valuel[-1][-1]

if __name__ == '__main__':
    N = int(input())
    vlists= list(map(int, input().split()))
    weights = list(map(int, input().split()))
    T = int(input())
    print('weights:', weights)
    print('valist:', vlists)

    bag(n=N, c=T, wlist=weights, vlist=vlists)

