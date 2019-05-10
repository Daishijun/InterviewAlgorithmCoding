# -*- coding: utf-8 -*-
# @Date    : 2018/6/13
# @Time    : 13:52
# @Author  : Daishijun
# @File    : sumtwo.py
# Software : PyCharm
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#
#         lenth = len(nums)
#         hasharr = [0]*(lenth+5)
#         arr2 =[0]*(lenth+5)
#         for i in range(lenth):
#             a = nums[i] % 13
#             while arr2[a] !=0:
#                 a+=1
#                 if i == lenth:
#                     i = 0
#             hasharr[a] = nums[i]
#             arr2[a] = 1
#
#         tarhash = (target-) % 13
#         while tarhash<(lenth+5):
#             if arr2[tarhash] ==1:
#                 if hasharr[]





if __name__ == '__main__':
    # solution = Solution()
    # print(solution.twoSum([3, 3], target=6))

    lista = [1,2,3,4,5,6,7]
    proleft = 1
    lists = []
    for i in range(len(lista)):
        lists.append(proleft)
        proleft*=lista[i]
    proright = 1
    for j in range(len(lista)-1, -1, -1):
        lists[j]*=proright
        proright*=lista[j]
    print(lists)





