#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/1 21:17
# @Author   : Daishijun
# @Site     : 
# @File     : p5.py
# @Software : PyCharm

t, k = list(map(int, input().split()))
# from scipy.special import comb

# def factorial_(n):
#     res = 1
#     for i in range(2, n+1):
#         res = res*i
#     return res

def comb_1(n,m):
    resm = 1
    resn = 1
    for i in range(2,m+1):
        resm = resm*i
    resn = resm
    for i in range(m+1,n+1):
        resn = resn*i
    resc = 1
    for i in range(2, n-m+1):
        resc = resc*i

    return resn//(resc*resm)

def getmethod(m,k):
    if m<k:
        return 1
    else:
        times = m//k
        res = 0
        for w in range(times+1):
            total = m-w*(k-1)
            res +=  comb_1(total, w)
        return res


checklist = []
for i in range(t):
    checklist.append(list(map(int, input().split())))


for a,b in checklist:

    res = 0
    for i in range(a, b + 1):
        res += getmethod(i,k)
    print(int(res)%(10**9+7))



# t, k = list(map(int, input().split()))
# from scipy.special import comb
# def getmethod(m,k):
#     if m<k:
#         return 1
#     else:
#         times = m//k
#         res = 0
#         for w in range(times+1):
#             total = m-w*(k-1)
#             res +=  comb(total, w)
#         return res
#
#
# checklist = []
# for i in range(t):
#     checklist.append(list(map(int, input().split())))
#
#
# for a,b in checklist:
#
#     res = 0
#     for i in range(a, b + 1):
#         res += getmethod(i,k)
#     print(int(res)%(10**9+7))


