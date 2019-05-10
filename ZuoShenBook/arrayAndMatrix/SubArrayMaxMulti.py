# -*- coding: utf-8 -*-
# @Date    : 2019/5/7
# @Time    : 8:54
# @Author  : Daishijun
# @File    : SubArrayMaxMulti.py
# Software : PyCharm

'''
数组中子数组的最大累乘积
'''

def maxProduct(arr):
    if not arr or len(arr) ==0:
        return 0
    mmax = arr[0]    #以arr[i-1]截尾的最大累乘积
    mmin = arr[0]    #以arr[i-1]结尾的最小累乘积
    res = arr[0]

    for i in range(1, len(arr)):    #一轮循环得到以第i位结尾的最大和最小累乘积
        maxEnd = mmax * arr[i]
        minEnd = mmin * arr[i]
        mmax = max([maxEnd, minEnd, arr[i]])
        mmin = min([maxEnd, minEnd, arr[i]])
        res = max(mmax, res)
    return res

if __name__ == '__main__':
    arr = [-2.5, 4, 0, 3, 0.5, 8, -1]
    print(maxProduct(arr))
