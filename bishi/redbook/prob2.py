#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/3 19:42
# @Author   : Daishijun
# @Site     : 
# @File     : prob2.py
# @Software : PyCharm

N = int(input())

mapd = [[0]*N for i in range(N)]

for i in range(N):
    rows = input()

    for j in range(len(rows)):
        mapd[i][j] = 1 if rows[j] == '#' else 0
        if rows[j] == 'S':
            start = [i,j]
        elif rows[j] == 'E':
            end = [i,j]

queue = []
det = [[1,0],[-1,0],[0,-1],[0,1]]

queue.append(start)

def findres(queue):
    res = -1
    path = 0
    while queue:
        level_len = len(queue)
        while level_len:
            ox,oy = queue.pop(0)
            level_len -=1
            for dx, dy in det:
                nx, ny = ox+dx, oy+dy
                if nx==-1:
                    nx = N-1
                if nx == N:
                    nx = 0
                if ny == -1:
                    ny = N-1
                if ny == N:
                    ny = 0
                if nx == end[0] and ny==end[1]:
                    res = path+1
                    return res
                if mapd[nx][ny] == 0:
                    mapd[nx][ny] = 1
                    queue.append((nx,ny))
        path +=1
    return res

print(findres(queue))

