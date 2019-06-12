# -*- coding: utf-8 -*-
# @Date    : 2019/6/12
# @Time    : 9:11
# @Author  : Daishijun
# @File    : findRepeatNum.py
# Software : PyCharm

'''Leetcode 287 寻找重复数
    剑指offer   Page 41
'''
'''数字在1-n之间'''
'''O(1)的空间
做法将每个index位置上的数字视为链表的next指针，这样如果出现重复数字，说明肯定有两个或者以上的index位置
指向相同的next，相当于链表中有环，问题转化为找链表中的环的入口
'''
class Solution:
    def findDuplicate(self, nums) -> int:
        if not nums or len(nums)<2:
            return -1
        # slow = nums[0]
        slow = 0
        # fast = nums[nums[0]]
        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
            print('first, slow:{}, fast:{}'.format(slow, fast))
        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
            print('second, slow:{}, fast:{}'.format(slow, fast))
        return slow

'''剑指的做法：
    将数值的范围进行二分，然后多次遍历数组，查找在这个范围中数字出现的次数
'''
class Solution:
    def findDuplicate2(self, nums) -> int:
        if not nums or len(nums)<2:
            return -1
        left = 1
        right = len(nums)-1
        while right>=left:
            mid = (left+right)>>1
            count = self.countRange(nums, left, mid)
            if left == right:
                if count>1:
                    return left
                else:
                    break    #最后缩小到一个数字了，还是没有发现重复，即count==1或者==0（允许某个数字缺失）.
            if count > (mid-left+1):
                right = mid
            else:
                left = mid+1
        return -1

    def countRange(self, nums, left, right):
        if not nums or len(nums)==0:
            return 0
        count = 0
        for num in nums:
            if num >= left and num <= right:
                count +=1
        return count

if __name__ == '__main__':
    nums = [1,3,4,2,2]
    S = Solution()
    # print(S.findDuplicate(nums))
    print(S.findDuplicate2(nums))

