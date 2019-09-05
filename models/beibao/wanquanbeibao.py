#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/3 18:58
# @Author   : Daishijun
# @Site     : 
# @File     : wanquanbeibao.py
# @Software : PyCharm


import numpy as np
def solve3(vlist,wlist,totalWeight,totalLength):
    """完全背包问题"""
    resArr = np.zeros((totalWeight)+1,dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])
    return resArr[-1]

if __name__ == '__main__':
    v = [0,60,100,120]
    w = [0,10,20,30]
    weight = 50
    n = 3
    result = solve3(v,w,weight,n)
    print(result)