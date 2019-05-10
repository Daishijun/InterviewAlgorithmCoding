# -*- coding: utf-8 -*-
# @Date    : 2019/4/8
# @Time    : 18:40
# @Author  : Daishijun
# @File    : baidu3.py
# Software : PyCharm

N, M = list(map(int, input().split()))
cout = 1
def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    res = power(base, exp>>1)
    res *= res
    if exp&1 == 1:
        res *=base
    return res

if N ==1:
    print(1)
else:
    midnum = N-1
    cout *=(M-2)
    # cout *= pow((M-1), midnum-1)
    cout *= power((M-1), midnum-1)

    print(cout%(10**9+7))

# def add(a,b):
#     if a == 0:
#         return b
#     return add((a&b)<<1, a^b)
#
# def mul(a, b):
#     s = 0
#     while b:
#         if b&1 :
#             s = add(s, a)
#         a = a<<1
#         b = b>>1
#     return s
# if N == 1:
#     print(1)
# else:
#     midnum = N-1
#     cout = mul(cout,M-2)
#     for i in range(midnum-1):
#         cout = mul(cout, M-1)
#     print(cout)