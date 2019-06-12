# -*- coding: utf-8 -*-
# @Date    : 2019/5/19
# @Time    : 12:32
# @Author  : Daishijun
# @File    : arrayPartition.py
# Software : PyCharm

'''
数组的partition调整
'''

'''补充问题'''
def sortarray(arr):
    if not arr or len(arr)<2:
        return
    left = -1
    index = 0
    right = len(arr)
    while index<right:
        if arr[index] == 0:
            arr[left+1], arr[index] = arr[index], arr[left+1]
            left +=1
            index +=1
        elif arr[index] == 1:
            index +=1
        else:
            arr[right-1], arr[index] = arr[index], arr[right-1]
            right -=1

if __name__ == '__main__':
    arr = [0,2,1,2,0,1,2]
    sortarray(arr)
    print(arr)