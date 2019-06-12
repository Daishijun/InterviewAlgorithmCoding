# -*- coding: utf-8 -*-
# @Date    : 2019/6/6
# @Time    : 9:09
# @Author  : Daishijun
# @File    : perfectSquare.py
# Software : PyCharm

'''LeetCode 279  完全平方数'''
'''
!!!!!!这道题用dp不行。会超时。
'''

import math

def sqrt(num):
    r = num//2
    l = 1
    while l <= r:
        mid = (l+r)>>1
        if mid*mid >num:
            r = mid-1
        elif mid * mid == num:
            return mid
        else:
            l = mid +1
    return l-1

def perfectsquare(target):
    if target<=0:
        return 0
    # largest = int(math.sqrt(target))
    tar = target
    largest = 0
    if tar<4:
        largest = 0
    else:
        r = tar>>1
        l = 1
        while l<=r:
            mid = (l+r)>>1
            if mid*mid == tar:
                largest = mid
                break
            elif mid * mid > tar:
                r = mid -1
            else:
                l = mid +1
        largest = l - 1 if largest == 0 else largest

    numlist = [ i**2 for i in range(largest+1, 0, -1)]
    return process(numlist, 0, target)



def process(numlist,index, rest):
    if index == len(numlist):
        return 0 if rest == 0 else -1
    res = -1
    k = 0
    while k*numlist[index] <= rest:
        renext = process(numlist, index+1, rest-k*numlist[index])
        if renext !=-1:
            res = renext+k if res == -1 else min(res, renext+k)
        k+=1
    return res

def perfectsquare2(target):
    if target<=0:
        return 0
    # largest = int(math.sqrt(target))
    tar = target
    largest = 0
    if tar<4:
        largest = 1
    else:
        r = tar>>1
        l = 1
        while l<=r:
            mid = (l+r)>>1
            if mid*mid == tar:
                largest = mid
                break
            elif mid * mid > tar:
                r = mid -1
            else:
                l = mid +1

        largest = l-1 if largest == 0 else largest

    numlist = [ i**2 for i in range(largest, 0, -1)]
    print(numlist)
    dp = [-1 for i in range(target +1 )]
    dp[0] = 0
    for i in range(len(numlist)):
        for j in range(numlist[i],target+1):
            if dp[j-numlist[i]] !=-1:
                if dp[j] == -1:
                    dp[j] = dp[j-numlist[i]]+1
                else:
                    dp[j] = min(dp[j], dp[j-numlist[i]]+1)
    return dp[target]

def perfectsquare3(target):
    if target<=0:
        return 0
    # largest = int(math.sqrt(target))
    dp = [float('inf') for i in range(target+1)]
    dp[0] = 0
    for i in range(target+1):
        j = 1
        while j*j<= i:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j +=1
    return dp[target]


'''用四平方定理'''
def numSquares(num):
    while num%4 == 0:
        num//=4
    if num%8 == 7:
        return 4
    a = 0
    while a**2 <=num:    #暴力看能不能拆成两个平方数的和
        b = int((num-a**2)**0.5)
        if a**2 + b**2 == num:
            return (not not a) + (not not b)
        a +=1
    return 3


if __name__ == '__main__':
    target = 9
    print(perfectsquare(target))
    print(perfectsquare2(target))
    print(perfectsquare3(target))
    print(numSquares(target))





