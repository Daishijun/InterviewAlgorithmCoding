# -*- coding: utf-8 -*-
# @Date    : 2019/6/12
# @Time    : 16:59
# @Author  : Daishijun
# @File    : maxMinusMinLessOrEqualNumSubarrNum.py
# Software : PyCharm

'''最大值减去最小值小于或等于num的子数组数量'''
def getNum(arr, target):
    if not arr or len(arr) == 0:
        return 0
    qmin = []
    qmax = []
    left = 0
    right = 0
    res = 0
    while left<len(arr):
        while right < len(arr):
            # if qmin == [] or qmin[-1] !=right:
            while qmin and arr[qmin[-1]]>= arr[right]:
                qmin.pop()
            qmin.append(right)
            while qmax and arr[qmax[-1]] <= arr[right]:
                qmax.pop()
            qmax.append(right)

            if arr[qmax[0]] - arr[qmin[0]] > target:
                break
            right +=1
        res += right - left
        if qmin[0] == left:
            qmin.pop(0)
        if qmax[0] == left:
            qmax.pop(0)
        left +=1
    return res

if __name__ == '__main__':
    arr = [1,2,3]
    target = 2
    print(getNum(arr, target))