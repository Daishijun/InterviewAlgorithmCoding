#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/4 12:09
# @Author   : Daishijun
# @Site     : 
# @File     : snapShotArrayprac3.py
# @Software : PyCharm

'''5149 快照数组'''

class SnapshotArray:

    def __init__(self, length: int):
        self.arraylist = [[] for i in range(length) ]
        self.setdict = {}
        self.snapid = 0

    def set(self, index: int, val: int) -> None:
        self.setdict[index] = val

    def snap(self) -> int:
        for index, val in self.setdict.items():
            self.arraylist[index].append([self.snapid, val])
        self.setdict = {}
        self.snapid +=1
        return self.snapid-1
    def get(self, index: int, snap_id: int) -> int:
        l = 0
        r = len(self.arraylist[index])-1
        while l<=r:
            m = (l+r)>>1
            if self.arraylist[index][m][0] <= snap_id:
                l = m+1
            else:
                r = m-1
        if r<0:
            return 0
        else:
            return self.arraylist[index][r][1]