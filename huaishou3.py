# -*- coding: utf-8 -*-
# @Date    : 2019/4/13
# @Time    : 16:39
# @Author  : Daishijun
# @File    : huaishou3.py
# Software : PyCharm



T = int(input())
for t in range(T):
    [N, M] = list(map(int, input().split()))
    vallist = list(map(int, input().split()))
    cost = [[20000 for i in range(N)] for j in range(N)]
    for m in range(M):
        [u,v,cos] = list(map(int, input().split()))
        cost[u][v] = cos
    mindis = None
    mindisp = None
    visited = []
    for i in range(len(vallist)):
        backl = vallist.copy()
        if i not in visited:
            mindisp = i
            mindis = vallist[i]
            visited.append(i)
            break
    for j in range(len(cost)):
        if cost[mindisp-1][j] < 20000:
            upd = mindis + cost[mindisp-1][j]
            if vallist[j+1] > upd:
                vallist[j+1] = upd
    print(min(vallist))

