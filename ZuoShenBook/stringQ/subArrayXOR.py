# -*- coding: utf-8 -*-
# @Date    : 2019/4/26
# @Time    : 10:21
# @Author  : Daishijun
# @File    : subArrayXOR.py
# Software : PyCharm

'''
子数组的最大异或和
'''
#数组的异或和：数组里的所有数异或起来

def maxXorSubarray1(arr):
    if not arr or len(arr)==0:
        return 0
    eor = []
    eor.append(arr[0])
    for i in range(1,len(arr)):
        eor.append(eor[-1]^arr[i])
    # print('eor:',eor)
    maxnum = -float('inf')
    for i in range(len(arr)):
        for j in range(i+1):
            if j==0:
                maxnum = max(maxnum, eor[i])
            else:
                maxnum = max(maxnum, eor[i] ^ eor[j-1])
    return maxnum

if __name__ =='__main__':
    arr = [3, -28, -29, 2]
    print(maxXorSubarray1(arr))