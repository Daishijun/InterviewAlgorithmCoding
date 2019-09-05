#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/5 9:37
# @Author   : Daishijun
# @Site     : 
# @File     : judgeStringLetterOnce.py
# @Software : PyCharm

'''判断字符数组中是否所有的字符都只出现过一次'''

'''方法一：用map记录词频，时间O(N)，空间O(N )'''

'''方法二: 堆排序，然后从头比较相邻字符。时间O(NlogN)，空间O(1)【非递归实现堆排序】
    原代码用JAVA所以可以直接比较ASCII码大小，python中需要ord()函数
'''
#大根堆
def heapInsert(chas, i):
    parent = 0
    while i != 0:
        parent = (i-1)>>1
        if chas[parent] < chas[i]:
            chas[parent], chas[i] = chas[i], chas[parent]
            i = parent

        # for string
        # if ord(chas[parent]) < ord(chas[i]):
        #     chas[parent], chas[i] = chas[i], chas[parent]
        #     i = parent
        else:
            break

def heapify(chas, i, size):
    left = i*2+1    #因为下标i从0开始记
    right = i*2+2
    largest = i
    while left<size:
        if chas[left]>chas[i]:
            largest = left
        if right<size and chas[right]>chas[largest]:
            largest = right

        #for string
        # if ord(chas[left])>ord(chas[i]):
        #         #     largest = left
        #         # if right<size and ord(chas[right])>ord(chas[largest]):
        #         #     largest = right

        if largest != i:
            chas[largest], chas[i] = chas[i], chas[largest]
        else:
            break
        i = largest
        left = i*2+1
        right = i*2+2

def heapsort(chas):
    for i in range(len(chas)):
        heapInsert(chas, i)
    for i in range(len(chas)-1,-1,-1):
        chas[0], chas[i] = chas[i], chas[0]    #最大值放在末尾， 然后从堆顶开始调整顺序
        heapify(chas, 0, i)

def isUnique2(chas):
    if chas == None:
        return True
    heapsort(chas)
    for i in range(1, len(chas)):
        if chas[i] == chas[i-1]:
            return False
    return True

if __name__ == '__main__':
    numlist = [1,5,3,7,8,2,9]
    print(isUnique2(numlist))