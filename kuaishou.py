# -*- coding: utf-8 -*-
# @Date    : 2019/4/13
# @Time    : 14:43
# @Author  : Daishijun
# @File    : kuaishou.py
# Software : PyCharm

# str1, str2 = input().split(',')
# print(str1)
# print(str2)



def missingNumber(nums):


    length = len(nums) + 1
    l = [-1] * (length)
    for n in nums:
        l[n] = 1
    for i in range(len(l)):
        if l[i] < 0:
            return i

def missing(nums):
    res = len(nums)
    for i in range(res):
        res ^=(i^nums[i])
    return res

if __name__ == '__main__':
    try:

        numlist = list(map(int, input().split(',')))
        print(missing(numlist))
    except:
        print(0)
    # numlist = []

#
# class Solution {
# public int missingNumber(int[] nums) {
# int ans = nums.length;
# for (int i = 0;i < nums.length;i++)
# ans ^= i ^ nums[i];
#
#
# return ans;
# }
# }

# https://blog.csdn.net/carson0408/article/details/78634650