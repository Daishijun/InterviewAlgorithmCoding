# -*- coding: utf-8 -*-
# @Date    : 2019/4/23
# @Time    : 20:52
# @Author  : Daishijun
# @File    : meituan2.py
# Software : PyCharm

# arr = [[1,2,3,2],[2,5,2,3],[1,4,3,4]]

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


def getcount(arr):
    pset = set()
    for [x1, y1, x2, y2] in arr:
        if x1 == x2:
            if y1<=y2:
                for j in range(y1, y2+1):
                    pset.add((x1,j))
            else:
                for j in range(y2, y1+1):
                    pset.add((x1,j))
        elif y1 == y2:
            if x1<=x2:
                for i in range(x1, x2+1):
                    pset.add((i, y1))
            else:
                for i in range(x2, x1+1):
                    pset.add((i, y1))
    return len(pset)


print(getcount(arr))