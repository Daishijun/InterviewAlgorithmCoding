# -*- coding: utf-8 -*-
# @Date    : 2019/5/6
# @Time    : 20:36
# @Author  : Daishijun
# @File    : natrualNumSort.py
# Software : PyCharm

'''
自然数组的排序
'''

def sort1(arr):
    tmp = 0
    nextnum = 0
    for i in range(len(arr)):
        tmp = arr[i]
        while arr[i] !=i+1:
            nextnum = arr[tmp-1]
            arr[tmp-1] = tmp
            tmp = nextnum

def sort2(arr):
    tmp = 0
    for i in range(len(arr)):

        while arr[i] !=i+1:
            tmp = arr[i]    #还是老老实实借助辅助变量交换比较稳妥，这里直接交换的话，会因为arr[arr[]]两层导致无法正确交换。
            arr[i] = arr[tmp-1]
            arr[tmp-1] = tmp



if __name__ == '__main__':
    arr = [1,2,5,3,4]
    # sort1(arr)
    sort2(arr)
    print(arr)
