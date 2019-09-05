#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/3 15:48
# @Author   : Daishijun
# @Site     : 
# @File     : prac1.py
# @Software : PyCharm

n = int(input())

def getmaxtimes(n):
    res = 0
    while n:
        res +=n//5
        n= n//5
    return res

def func(n):
    if n<0:
        return 0
    t = 0
    res = 0
    for i in range(1,n+1):
        # if i%5==0:
        #     t = getmaxtimes(i)
        # res +=t
        res += getmaxtimes(i)
    return res


print(func(n))