# -*- coding: utf-8 -*-
# @Date    : 2019/5/7
# @Time    : 21:05
# @Author  : Daishijun
# @File    : shareCandies.py
# Software : PyCharm

'''
分糖果问题
'''
'''
原问题， 对相邻的得分一样的没有约束
'''

def nextMinIndex1(arr, start):
    for i in range(start, len(arr)-1):
        if arr[i] <= arr[i+1]:
            return i
    return len(arr)-1

def rightCands(arr, left, right):
    length = right-left+1
    return (length*(length+1))>>1

def candy1(arr):
    if not arr or len(arr) == 0:
        return 0
    index = nextMinIndex1(arr, 0)
    res = rightCands(arr, 0, index)
    index +=1
    lbase = 1    #上坡坡度
    rbase = 0
    rcandy = 0
    while index < len(arr):
        if arr[index] > arr[index-1]:    #上坡
            lbase +=1
            res += lbase
            index +=1
        elif arr[index] < arr[index-1]: #下坡
            nextind = nextMinIndex1(arr, index-1) #因为arr[index-1]的值更大，所以下坡的起点应该是index-1
            rcandy = rightCands(arr, index-1, nextind)
            nextind +=1
            rbase = nextind - index +1 #下坡坡度
            if lbase>rbase:
                rcandy -= rbase
            else:
                rcandy -=lbase
            res += rcandy
            lbase =1
            index = nextind
        else:
            res +=1
            lbase = 1
            index +=1
    return res

if __name__ == '__main__':
    num = 4
    import math
    print(math.sqrt(num))

