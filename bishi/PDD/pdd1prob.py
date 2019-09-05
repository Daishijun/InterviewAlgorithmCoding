#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/28 14:49
# @Author   : Daishijun
# @Site     : 
# @File     : pdd1prob.py
# @Software : PyCharm

'''升序数组'''



def process(A, B):
    less = float('-inf')
    more = float('inf')
    B.sort(reverse=True)
    for i in range(1,len(A)):
        if A[i-1] >= A[i]:
            index = i
            left = A[i-1]
            right = A[i]
            leftl = A[i-2] if i-2>-1 else float('-inf')
            rightr = A[i+1] if i+1 < len(A) else float('inf')
            break
    # print('index', index)
    findflag = False
    if leftl >= right:
        less = left
        more = rightr
        for num in B:
            if num > less and num < more:
                A[index] = num
                findflag = True
                break

    elif rightr <= left:
        less = leftl
        more = right
        for num in B:
            if num > less and num < more:
                A[index-1] = num
                findflag = True
                break
    else:
        #change index
        less =  left
        more = rightr
        for num in B:
            if num > less and num < more:
                A[index] = num
                findflag = True
                break
        if not findflag:
            less = leftl
            more = right
            for num in B:
                if num > less and num < more:
                    A[index - 1] = num
                    findflag = True
                    break
    return A, findflag

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))


A = [1,3,4,2,7,8,9]
B = [1,2,3,4,5,6,9,10]
A, flag = process(A, B)
if flag:
    # print(A)
    print(' '.join(map(str, A)))
else:
    print('NO')

