#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/1 20:41
# @Author   : Daishijun
# @Site     : 
# @File     : p4.py
# @Software : PyCharm

'''dandiaozhan'''

def maxBottom(hist):
    if not hist or len(hist) == 0:
        return 0
    maxScore = 0
    stack = []
    for i in range(0, len(hist)):
        while stack and hist[i]<=hist[stack[-1]]:
            j = stack.pop(-1)
            k = -1 if len(stack)==0 else stack[-1]
            curScore = hist[j] * (sum(hist[k+1:i]))
            maxScore = max(maxScore, curScore)
        stack.append(i)
    while stack:
        j = stack.pop(-1)
        k = -1 if len(stack) == 0 else stack[-1]
        curScore = hist[j] * (sum(hist[k+1:]))
        maxScore = max(maxScore, curScore)
    return maxScore

N = int(input())
nlist = list(map(int, input().split()))

print(maxBottom(nlist))