# -*- coding: utf-8 -*-
# @Date    : 2019/5/19
# @Time    : 11:43
# @Author  : Daishijun
# @File    : withoutSelfContinueMulti.py
# Software : PyCharm

'''不包含本位置值的累乘数组'''

'''分为可用除法，需要判断有没有0，有几个0的情况； 不用除法，左边累乘辅助数组*右边累乘辅助数组，注意两头的特殊情况'''

def product2(arr):
    if not arr or len(arr)<2:
        return None
    res = [0 for i in range(len(arr))]
    res[0] = arr[0]
    for i in range(1, len(arr)):
        res[i] = res[i-1]*arr[i]
    tmp =1    #表示从右侧的累乘
    for j in range(len(arr)-1, 0, -1):
        res[j] = res[j-1]*tmp
        tmp = tmp*arr[j]
    res[0] = tmp
    return  res

