# -*- coding: utf-8 -*-
# @Date    : 2019/6/5
# @Time    : 10:36
# @Author  : Daishijun
# @File    : shortestUnsortContinSubArr.py
# Software : PyCharm

'''leetcode 581 最短无序连续子数组'''

'''思路一：备份个数组，然后排序，从首尾边找到第一个数值不相等的位置。
    思路二：从左到右，先找到不满足递增关系的点，然后记录从点后的最小值，
            遍历一遍找到这个最小值应该插入的位置
            从右向左，找到不满足递减关系的点，然后记录此后的最大值，遍历一遍找到这个
            最大值应该插入的位置。
            两个插入位置中间都是需要排序的
'''


class Solution:
    def findUnsortedSubarray(self, nums) -> int:

        index = 1
        while index< len(nums) :
            if nums[index] < nums[index-1]:
                submin = nums[index]
                break
            index +=1
        if index == len(nums):
            return 0
        for i in range(index, len(nums)):
            if submin > nums[i]:
                submin = nums[i]
        left = 0
        while left<len(nums):
            if submin <nums[left]:
                break
            left +=1

        ind  = len(nums)-2
        while ind > -1:
            if nums[ind] > nums[ind+1]:
                submax = nums[ind]
                break
            ind -=1
        print('ind:', ind)
        for j in range(ind, -1, -1):
            if submax < nums[j]:
                submax = nums[j]
        right = len(nums)-1
        while right > -1:
            if nums[right] <submax:
                break
            right -=1
        print('submin:{}  submax{}'.format(submin, submax))
        print('left:{}  right:{}'.format(left, right))
        return right - left +1

if __name__ == '__main__':
    nums = [1,5,3,2,4]
    S = Solution()
    print(S.findUnsortedSubarray(nums))

