#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/1 15:22
# @Author   : Daishijun
# @Site     : 
# @File     : p4.py
# @Software : PyCharm


n, m, k = list(map(int, input().split()))
if n>m:
    k = k+(n-m)**2
elif n<m:
    k = k+ (m-n)**2

print('k=',k)

i = 1
while (1+i)*i<2*k:
    i +=1
# print('i=',i)
ind = k-(i)*(i-1)//2  #第3个
ind = (i-ind)//2  # 倒数第几个
res = (n-(i-1)+ind) * (n-ind)

print(res)