#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/18 11:07
# @Author   : Daishijun
# @Site     : 
# @File     : taskSchedule.py
# @Software : PyCharm

'''Leetcode 621 任务调度器'''

'''
应该算是一种贪心，先计算词频最多的任务完成需要的最短时间，把其他的任务穿插进去，如果其他任务不够
填满空位，则说明词频最多任务完成所需的最短时间就是结果；
如果能够填满空位，且还有剩余，那么任务就可以交替完成不需要等待，即task长度为最短时间。
'''

class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        count = [0] * 26
        for t in tasks:
            count[ord(t) - ord('A')] +=1
        maxnum = 0
        count.sort()
        for i in range(len(count)-1, -1, -1):
            if count[i] != count[-1]:
                break
            maxnum+=1
        res = max((count[-1]-1) * (n+1) + maxnum, len(tasks))
        return res

if __name__ == '__main__':

    mapdi = {1:9, 2:8, 3:7, 4:6}
    sortedmap = sorted(mapdi.items(), key=lambda x:x[1])
    print(sortedmap)