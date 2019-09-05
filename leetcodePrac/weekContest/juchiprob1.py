#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/4 10:35
# @Author   : Daishijun
# @Site     : 
# @File     : juchiprob1.py
# @Software : PyCharm

'''5147'''

class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        if len(nums) <3:
            return 0
        #偶数index大
        # tmp = 0
        # for i in range(0,len(nums),2):
        #     if i==0 :
        #         if nums[i]<=nums[i+1]:
        #             tmp += nums[i+1]-nums[i]+1
        #     elif i == len(nums)-1:
        #         if nums[i]<=nums[i-1]:
        #             tmp += nums[i-1]-nums[i]+1
        #     else:
        #         if nums[i]<=nums[i-1] or nums[i]<=nums[i+1]:
        #             tmp += max(nums[i-1], nums[i+1])-nums[i]+1
        tmp2 = 0
        for j in range(1, len(nums),2):
            if j==len(nums)-1:
                if nums[j]>=nums[j-1]:
                    tmp2 += nums[j]-nums[j-1]+1
            else:
                if nums[j]>=nums[j-1] or nums[j]>=nums[j+1]:
                    tmp2 += nums[j] - min(nums[j-1],nums[j+1])+ 1
        #奇数index大
        # tmp3 = 0
        # for j in range(1, len(nums),2):
        #     if j == len(nums)-1:
        #         if nums[j] <= nums[j-1]:
        #             tmp3 += nums[j-1] - nums[j]+1
        #     else:
        #         if nums[j] <=nums[j-1] or nums[j]<=nums[j+1]:
        #             tmp3 += max(nums[j-1], nums[j+1])-nums[j]+1
        tmp4 = 0
        for i in range(0, len(nums), 2):
            if i == 0:
                if nums[i]>=nums[i+1]:
                    tmp4 += nums[i]-nums[i+1]+1
            elif i == len(nums)-1:
                if nums[i]>=nums[i-1]:
                    tmp4 += nums[i] - nums[i-1] +1
            else:
                if nums[i] >= nums[i-1] or nums[i]>=nums[i+1]:
                    tmp4 += nums[i] - min(nums[i-1], nums[i+1])+1
        return min([tmp2,  tmp4])

# class Solution:
#     def movesToMakeZigzag(self, nums) -> int:
#         if len(nums) <3:
#             return 0
#         #中间大
#         tmp = 0
#         for i in range(1, len(nums),2):
#             if i == len(nums)-1:
#                 tmp += max(0, nums[i-1]-nums[i]+1)
#             else:
#                 if nums[i]<=nums[i-1] or nums[i]<=nums[i+1]:
#                     tmp += max(nums[i-1], nums[i+1])-nums[i]+1
#         tmp1 = 0
#         for i in range(1, len(nums), 2):
#             if i == len(nums)-1:
#                 tmp1 += max(0, nums[i]- nums[i-1]+1)
#             else:
#                 if nums[i] >= nums[i - 1] or nums[i]>=nums[i+1]:
#                     tmp1 += nums[i] - min(nums[i-1], nums[i+1])+1
#         return min(tmp1, tmp)
#
# class Solution:
#     def movesToMakeZigzag(self, nums) -> int:
#         if len(nums) < 3:
#             return 0
#
#         def cal(index, high):
#             tmp1 = 0
#             tmp2 = 0
#             if high:
#                 if index == len(nums)-1 and nums[index]<=nums[index-1]:
#                     pass
#
#                 if nums[index] <= nums[index-1] or nums[index]<=nums[index+1]:
#                     tmp1 += max(nums[index-1], nums[index+1])-nums[index]+1
#                     tmp2 += max(0, nums[index]-nums[index-1]+1) + max(0, nums[index]-nums[index+1]+1)
#                     if tmp1<=tmp2:
#                         nums[index] = nums[index] + tmp1
#                         return tmp1
#                     else:
#                         if nums[index]<=nums[index-1] :
#                             nums[index-1] = nums[index]-1
#                         if nums[index] <= nums[index+1]:
#                             nums[index+1] = nums[index]-1
#                         return tmp2
#             else:
#                 if nums[index] >= nums[index-1] or nums[index]>=nums[index+1]:
#                     tmp1 += nums[index]-min(nums[index-1], nums[index+1])+1
#                     tmp2 += max(0, nums[index-1]-nums[index]+1) + max(0, nums[index+1]-nums[index]+1)
#                     if tmp1<=tmp2:
#                         nums[index] = nums[index] - tmp1
#                         return tmp1
#                     else:
#                         if nums[index]>=nums[index-1] :
#                             nums[index-1] = nums[index]+1
#                         if nums[index] >= nums[index+1]:
#                             nums[index+1] = nums[index]+1
#                         return tmp2

if __name__ == '__main__':
    S = Solution()
    nums = [2,7,10,9,8,9]
    print(S.movesToMakeZigzag(nums))