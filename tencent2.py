# -*- coding: utf-8 -*-
# @Date    : 2019/4/7
# @Time    : 20:55
# @Author  : Daishijun
# @File    : tencent2.py
# Software : PyCharm


def Core(nums):


    backnums = list(set(nums))
    backnums.sort()
    print(backnums)


    # if len(backnums) == 0:
    #     mmin = 0
    # else:
    #     mmin = min(backnums)
    # print('back:', backnums)
    # print('num:', nums)
    # print(mmin)
    # for i in range(len(nums)):
    #     if nums[i] !=0:
    #         nums[i] -=mmin
if __name__ == '__main__':
    plist = list(map(int, input().split()))
    pplist = list(map(int, input().split()))
    [N, K] = plist
    nums = pplist
    for i in range(K):
        Core(nums)

