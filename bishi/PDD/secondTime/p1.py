#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/1 14:53
# @Author   : Daishijun
# @Site     : 
# @File     : p1.py
# @Software : PyCharm


input1 , input2 = input().split(';')
numlist, N = list(map(int, input1.split(','))), int(input2)

oulist = []
jilist = []
for num in numlist:
    if num%2==1:
        jilist.append(num)
    else:
        oulist.append(num)
oulist.sort(reverse=True)
jilist.sort(reverse=True)

relist = []
if N <= len(oulist):
    relist = oulist[:N]
else:
    relist = oulist + jilist[:N-len(oulist)]
print(','.join(map(str, relist)))