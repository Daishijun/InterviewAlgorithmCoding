#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/28 10:32
# @Author   : Daishijun
# @Site     : 
# @File     : SortAlg.py
# @Software : PyCharm

'''排序算法'''

'''
希尔排序
'''
def xierSort1(arr):
    gap = len(arr)//2
    while gap:
        for i in range(gap, len(arr)):    #相当于从每组的第二个元素开始向前进行插入排序，把每组的左侧变成有序区
            j = i
            while j-gap>=0 and arr[j] < arr[j-gap]:    #降序排列
                arr[j], arr[j-gap] = arr[j-gap], arr[j]    #从后向前逐渐交换位置
                j -=gap
        gap = gap//2

def xierSort2(arr):
    gap = len(arr)//2
    while gap:
        for i in range(gap, len(arr)):    #相当于从每组的第二个元素开始向前进行插入排序，把每组的左侧变成有序区
            j = i
            tmp = arr[j]

            while j-gap>=0 and tmp < arr[j-gap]:    #降序排列
                arr[j] = arr[j-gap]    #将每组较大的元素向后移动
                j -=gap
            arr[j] = tmp
        gap = gap//2

'''
堆排序
注意取堆顶的时候，把堆顶和最后一个元素换位置，堆的length-1，然后调整堆
'''

def sink(arr, index, length):    #下沉操作
    leftchild = 2*index+1
    rightchild = 2*index +2
    present = index    #present 就是一个寻找交换位置的标记
    if leftchild<length and arr[leftchild]>arr[present]:    #当前元素比左孩子还小，需要下移
        present = leftchild
    if rightchild<length and arr[rightchild]>arr[present]:
        present = rightchild

    if present!=index:    #移动过了
        arr[index], arr[present] = arr[present], arr[index]
        sink(arr, present, length)

def buildHeap(arr, length):
    for i in range(length//2, -1, -1):    #初始是最后一个有左右孩子的节点。
        sink(arr, i, length)

def heapSort(arr):
    length = len(arr)
    buildHeap(arr, length)
    for i in range(length-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        length -=1
        sink(arr, 0, length)





if __name__ == '__main__':
    arr = [8,9,1,7,2,3,5,4,6,0]
    xierSort2(arr)
    print(arr)
    arr = [8, 9, 1, 7, 2, 3, 5, 4, 6, 0]
    heapSort(arr)
    print(arr)
