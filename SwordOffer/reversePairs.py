# -*- coding: utf-8 -*-
# @Date    : 2019/5/22
# @Time    : 15:36
# @Author  : Daishijun
# @File    : reversePairs.py
# Software : PyCharm

'''剑指51 数组中的逆序对数'''

def InversePairCore(arr, copylist, start, end):
    if start == end:
        copylist[start] = arr[start]
        return 0
    mid = (start+end)>>1
    left = InversePairCore(copylist, arr, start, mid)
    right = InversePairCore(copylist, arr, mid + 1, end)

    l = mid
    r = end
    indexC = end
    count = 0
    while l>=start and r>=mid+1:
        if arr[l]>arr[r]:
            count += r-(mid+1)+1
            copylist[indexC] = arr[l]
            l -=1
            indexC -=1
        else:
            copylist[indexC] = arr[r]
            r -=1
            indexC -=1
    for i in range(l, start-1,-1):
        copylist[indexC] = arr[l]
        indexC -=1
    for j in range(r, mid, -1):
        copylist[indexC] = arr[r]
        indexC -=1
    return left+ right + count


def inversePairs(arr):
    if not arr:
        return 0
    copylist = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        copylist[i] = arr[i]
    count = InversePairCore(arr, copylist, 0, len(arr)-1)
    arr[:] = copylist[:]
    return count

def func(arr, left, right):
    if left == right:
        return 0
    mid = (left+right)>>1
    return func(arr, left, mid) + func(arr, mid+1, right) + merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    colist = [0 for i in range(right-left+1)]
    r = right
    l = mid
    index = right-left    #从colist后面开始填
    count = 0
    while l >= left and r >= mid+1:
        print('l:{l}, r:{r}'.format(l=l, r= r))
        print('arr[left]={left}    arr[right]={right}'.format(left =arr[l], right=arr[r]))
        if arr[l] > arr[r]:
            print('累加,',r-mid)
            count += r-mid
            colist[index] = arr[l]
            index -=1
            l -=1
        else:
            colist[index] = arr[r]
            index -=1
            r -=1
    for i in range(l, left-1, -1):
        colist[index] = arr[l]
        index -= 1
        l -= 1
    for j in range(r, mid, -1):
        colist[index] = arr[r]
        index -= 1
        r -= 1
    for i in range(len(colist)):
        arr[left] = colist[i]
        left +=1
    print('merge count:', count)
    return count

if __name__ =='__main__':
    arr = [7,5,6,4]
    print(inversePairs(arr))
    # print(func(arr, 0, len(arr)-1))
    print(arr)