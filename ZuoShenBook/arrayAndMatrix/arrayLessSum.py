# -*- coding: utf-8 -*-
# @Date    : 2019/5/6
# @Time    : 20:09
# @Author  : Daishijun
# @File    : arrayLessSum.py
# Software : PyCharm
'''
计算数组的小和， page392
'''
'''
借助归并排序，在合并过程中把小和“挤”出来
'''

def merge(arr, left, mid, right):
    '''
    :param arr: 归并排序的数组
    :param left: 合并的左数组的left下标
    :param mid: 合并的中间下标
    :param right: 合并的右侧下标
    :return:
    '''
    hlist = [0 for i in range(right-left+1)]    #用于存放排序后的数组
    hindex = 0
    i = left
    j = mid+1
    smallsum = 0
    while i <= mid and j <=right:
        if arr[i] <= arr[j]:
            smallsum += (arr[i] * (right - j + 1))   #这个必须在i++之前，否则下标就变化了

            hlist[hindex] = arr[i]
            hindex +=1
            i+=1


        else:
            hlist[hindex] = arr[j]
            hindex +=1
            j +=1
    while i<mid+1 or j < right+1 :
        if i<mid +1:
            hlist[hindex] = arr[i]
            hindex +=1
            i +=1
        else:
            hlist[hindex] = arr[j]
            hindex +=1
            j +=1
    for i in range(len(hlist)):
        arr[left+i] = hlist[i]
    return smallsum

def func(arr, left, right):
    if left == right:
        return 0
    mid = (left+right)>>1
    return func(arr, left, mid) + func(arr, mid+1, right) + merge(arr, left, mid, right)

def getSmallSum(arr):
    if not arr or len(arr) == 0:
        return 0
    return func(arr, 0, len(arr)-1)

if __name__ == '__main__':
    arr = [1,3,5,2,4,6]
    print(getSmallSum(arr))


