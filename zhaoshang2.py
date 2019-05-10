# -*- coding: utf-8 -*-
# @Date    : 2019/4/9
# @Time    : 21:01
# @Author  : Daishijun
# @File    : zhaoshang2.py
# Software : PyCharm
import heapq
class Solution:

    def __init__(self):
        self.maxlist = []
        self.minlist = []

    def Insert(self, num):

        if (len(self.maxlist) + len(self.minlist)) &1 ==0:  #偶数  ==>小堆
            if len(self.maxlist)>0 and num < -self.maxlist[0]:
                heapq.heappush(self.maxlist, -num)
                num = -heapq.heappop(self.maxlist)

            heapq.heappush(self.minlist, num)
        else:
            if len(self.minlist) >0 and num> self.minlist[0]:
                heapq.heappush(self.minlist, num)
                num = heapq.heappop(self.minlist)
            heapq.heappush(self.maxlist, -num)
    def GetMedian(self):
        size = len(self.minlist) + len(self.maxlist)
        if size == 0:
            raise Exception('No nums')
        median = 0
        if size&1 :
            median = self.minlist[0]
        else:
            median = (self.minlist[0] - self.maxlist[0])>>1
        return median


if __name__ == '__main__':
    # so = Solution()
    # num = [2,3,4,2,6,2,5,1]
    # size = 3
    # print(so.maxInWindows(num, size))

    a = 0 and 3
    print(a)
    print(type(a))
    al = []
    print(not al)