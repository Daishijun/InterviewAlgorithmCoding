# -*- coding: utf-8 -*-
# @Date    : 2019/4/30
# @Time    : 18:42
# @Author  : Daishijun
# @File    : minKinArray.py
# Software : PyCharm

'''import sys
# sys.setrecursionlimit(100000)
找到无序数组中最小的K个数
'''
#


#维护大根堆做法：    时间复杂度： O(N logk)

#建堆和调整堆
def heapInsert(arr, value, index):
    arr[index] = value
    while index>0:
        parent = (index-1)>>1
        if arr[parent] < arr[index]:
            arr[parent], arr[index] = arr[index], arr[parent]
            index = parent
        else:
            break

def heapify(arr, index, heapsize):
    left = index*2+1
    right = index*2+2
    largest = index
    while left<heapsize:
        if arr[left]>arr[index]:
            largest = left
        if right<heapsize and arr[right] > arr[largest]:
            largest = right
        if largest !=index:
            arr[largest], arr[index] = arr[index], arr[largest]
        else:
            break
        index = largest
        left = index*2+1
        right = index*2+2

def getMinKNumsByHeap(arr, k):
    if k<1 or k > len(arr):
        return arr
    kHeap = [0 for i in range(k)]
    for i in range(k):
        heapInsert(kHeap, arr[i], i)
    print('init kHeap:', kHeap)
    for i in range(k, len(arr)):
        if arr[i] < kHeap[0]:
            kHeap[0] = arr[i]
            heapify(kHeap, 0, k)
    return kHeap


################################################
#BFPRT 算法，在O(N)的时间复杂度下，从无序数组中找到第k小的数    ！！！原算法解决的是找到第k个数，即只找到一个数。

def insertionSort(arr, begin, end):
    for i in range(begin+1, end+1):
        for j in range(i, begin, -1):    #下边要用到j-1,所以j不能取到begin
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

def getMedian(arr, begin, end):
    insertionSort(arr, begin, end)
    indexsum = end + begin
    mid = (indexsum//2)+(indexsum%2)
    return arr[mid]

def partition(arr, begin, end, pivotValue):    #根据划分点pivot来将arr的数据划分成块，小于在左，大于子右。
    small = begin - 1
    index = begin
    big = end+1
    while index !=big:
        if arr[index] < pivotValue:
            small +=1
            arr[index], arr[small] = arr[small], arr[index]
            index +=1
        elif arr[index] > pivotValue:
            big -=1
            arr[index], arr[big] = arr[big], arr[index]
        else:
            index +=1
    range = []
    range.append(small+1)
    range.append(big-1)
    return range

def medianOfMedians(arr, begin, end):    #这里在处理中位数数组的时候，就不再使用插入排序再找中位数了，而是使用找arr中最小的第k个数的select()来做。原因是：这样刻意规避中位数数组元素过多时时间复杂度过高。
    elecounts = end - begin+1
    offset = 1 if elecounts%5!=0 else 0
    mArr = [0 for i in range(elecounts//5+offset)]

    for i in range(len(mArr)):
        beginI = begin + i*5
        endI = beginI +4
        mArr[i] = getMedian(arr, beginI, min(endI, end))
    return select(mArr, 0, len(mArr)-1, len(mArr)//2)    #返回中位数数组的中位数    !!!注意这里用来select的不是arr了，而是中位数数组

def select(arr, begin, end, i):    #找第i+1小的数, 借鉴快排思想。 i表示的是arr的下标，所以排序后第i+1小的数字，下边应该是i，‘下标从0开始计算’
    if begin == end:
        return arr[begin]
    pivot = medianOfMedians(arr, begin, end)
    pivotRange = partition(arr, begin, end, pivot)
    if i >= pivotRange[0] and i <= pivotRange[1]:
        return arr[i]    #这里的arr已经在partition()中改变了
    elif i< pivotRange[0]:
        return select(arr, begin, pivotRange[0]-1, i)
    else:
        return select(arr, pivotRange[1]+1, end, i)

def copyArray(arr):
    copyarr = arr.copy()
    return copyarr

def getMinKthByBFPRT(arr, K):    #K ==> 第K小的数字
    copyarr = copyArray(arr)
    return select(copyarr, 0 , len(copyarr)-1, K-1)    #第K小的数，对应的下标应是K-1

def getMinKNumsByBFPRT(arr, k):
    if k <1 or k> len(arr) :
        return arr
    minKth = getMinKthByBFPRT(arr, k)    #第k小的数字（算上了重复值的情况），后续可以根据这个数来筛选出最小的K个数
    res = [0 for i in range(k)]
    index = 0    # res[] 里的下标
    for i in range(len(arr)):
        if arr[i] <minKth:
            res[index] = arr[i]
            index +=1
    for j in range(index, k):    #如果比第K小的数字没有填满res[]，说明最小的K个数字中包含了第K小的数，如果第K小的数有多个重复值，也要加入到res[]中。
        res[j] = minKth
        j +=1
    return res








if __name__ == '__main__':
    arr = [1,5,8,3,0,2,6]
    k = 3
    print(getMinKNumsByHeap(arr, k))

    print(getMinKNumsByBFPRT(arr, k))

    # insertionSort(arr, 0, len(arr)-1)
    # print(arr)
    # print(getMedian(arr, 0, len(arr)-1))
    # print(arr)


