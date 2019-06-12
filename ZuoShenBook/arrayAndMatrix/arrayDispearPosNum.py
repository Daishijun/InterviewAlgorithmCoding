# -*- coding: utf-8 -*-
# @Date    : 2019/5/19
# @Time    : 14:32
# @Author  : Daishijun
# @File    : arrayDispearPosNum.py
# Software : PyCharm

'''
数组中未出现的最小正整数
'''
'''给的是一个无序整型数组，找到数组中没出现的最小正整数'''

def missNum(arr):
    if not arr:
        return 0
    left = 0
    right = len(arr)
    while (left<right):
        if arr[left] == left+1:
            left+=1
        elif arr[left]<=left or arr[left] > len(arr) or arr[arr[left]-1] == arr[left]:
            arr[left] = arr[right-1]
            right -=1
        else:    #如果数值在[left+1,right]内，但是又不满足arr[left] == left+1， 说明arr[left]的数值应该放在arr[left]-1的位置上去，所以交换两个位置的数字。
            tmp =arr[left]
            arr[left] = arr[arr[left]-1]
            arr[arr[left]-1] = tmp
    return left+1    #不包含的正整数

if __name__ =='__main__':
    arr = [-1,2,3,4]
    print(missNum(arr))