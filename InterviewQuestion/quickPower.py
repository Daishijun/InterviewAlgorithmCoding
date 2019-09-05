#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/18 20:08
# @Author   : Daishijun
# @Site     : 
# @File     : quickPower.py
# @Software : PyCharm

'''快速幂'''

'''这里并没有考虑指数项为负数的情况， 指数项为负的时候，需要最后取倒数
    而且也并没有考虑指数项为分数的情况。
'''
def quickp(a, n):
    res = 1
    while n:
        if n&1:
            res = res*a
        n = n>>1
        a = a*a
    return res

#求a**n % mod   快速幂取模
def quickpowerMode(a, n , mod):
    res = 1
    while n:
        if n&1:
            res = (res*a)%mod
        n = n>>1
        a = (a*a)%mod
    return res

if __name__ == '__main__':
    a = 2
    n = 10
    mod = 5
    print(quickp(a, n))
    print(quickpowerMode(a, n, mod))
    print(a**n%mod)