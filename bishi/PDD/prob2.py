#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/28 15:24
# @Author   : Daishijun
# @Site     : 
# @File     : prob2.py
# @Software : PyCharm

stringlist = input().split()
hlist = [0]*26

for string in stringlist:
    hlist[ord(string[0])- ord('A')] +=1
    hlist[ord(string[-1])- ord('A')] -=1
print(hlist==[0]*26)