# -*- coding: utf-8 -*-
# @Date    : 2019/4/28
# @Time    : 21:26
# @Author  : Daishijun
# @File    : duxiaoman2.py
# Software : PyCharm

import collections

n = int(input())
alist = list(map(int, input().split()))

lcounter = collections.Counter()
rcounter = collections.Counter(alist)

l_c = 0
r_c = n
res = [0 for i in range(n-1)]
for i in range(n-1):
    lcounter[alist[i]] +=1
    l_c +=1
    rcounter[alist[i]] -=1
    r_c -=1
    res[i] = res[i-1] + (r_c - rcounter[alist[i]]) - (l_c - lcounter[alist[i]])

print(' '.join(map(str, res)))