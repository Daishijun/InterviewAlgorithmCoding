#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/28 16:21
# @Author   : Daishijun
# @Site     : 
# @File     : prob3.py
# @Software : PyCharm

N, M = list(map(int, input().split()))
Pilist = list(map(int, input().split()))
mapdict = {}
for i in range(M):
    Ai, Bi = list(map(int, input().split()))
    if Bi in mapdict.keys():
        mapdict[Bi].append(Ai)
    else:
        mapdict[Bi] = [Ai]
# print(mapdict)

nonyilai = []
for i in range(1,N+1):
    if i not in mapdict.keys():
        nonyilai.append(i)
        for k, li in mapdict.items():
            if i in li:
                mapdict[k].pop(mapdict[k].index(i))

nonyilai.sort(key=lambda x:Pilist[x-1])
backlist = list(mapdict.keys())
while backlist:
    tmplist = []
    for k, vlist in mapdict.items():
        if vlist == []:
            mapdict[k] = None
            backlist.remove(k)
            tmplist.append(k)
    tmplist.sort(key=lambda x:Pilist[x-1])
    for value in tmplist:
        for k, vl in mapdict.items():
            if not vl:
                continue
            if value in vl:
                mapdict[k].pop(mapdict[k].index(value))
    nonyilai = nonyilai+ tmplist
# print(nonyilai)
print(' '.join(map(str, nonyilai)))