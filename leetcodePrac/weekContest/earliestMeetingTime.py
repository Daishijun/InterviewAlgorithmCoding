#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/29 23:39
# @Author   : Daishijun
# @Site     : 
# @File     : earliestMeetingTime.py
# @Software : PyCharm

'''Leetcode 3'''


#并查集
class Element():    #封装下节点
    # check = 7
    def __init__(self, value):
        self.value = value

class UnionFindSet():
    def __init__(self, vallist):    #根据list创建一个原始的并查集，即每个节点为独立的代表节点
        self.elementMap = {}
        self.fatherMap = {}
        self.rankMap = {}
        for val in vallist:
            ele = Element(val)
            self.elementMap[val] = ele    #根据数值来找到封装的element， 这样就不用去查找特定value值的element了。
            self.fatherMap[ele] = ele
            self.rankMap[ele] = 1

    def findHead(self, element):    #找到代表节点
        path = []    #记录element直到代表节点的路径，用来路径压缩，打平并查集
        while self.fatherMap[element] != element:
            path.append(element)
            element = self.fatherMap[element]

        for ele in path:    #路径压缩
            self.fatherMap[ele] = element
            #这里不需要处理rankmap , 因为是在一个链下进行操作，集合内元素没有增加或者减少
        return element

    def isSameSet(self, val1, val2):
        if val1 in self.elementMap.keys() and val2 in self.elementMap.keys():
            return self.findHead(self.elementMap[val1]) == self.findHead(self.elementMap[val2])
        return False

    def union(self, val1, val2):
        if val1 in self.elementMap.keys() and val2 in self.elementMap.keys():
            aF = self.findHead(self.elementMap[val1])
            bF = self.findHead(self.elementMap[val2])
            if aF != bF:
                big = aF if self.rankMap[aF] > self.rankMap[bF] else bF
                small = bF if big == aF else aF
                self.fatherMap[small] = big
                self.rankMap[big] += self.rankMap[small]
                self.rankMap.pop(small)

class Solution:
    def earliestAcq(self, logs, N: int) -> int:
        res = -1
        nlist = list(range(N))
        unionset = UnionFindSet(nlist)
        logsmap = {}
        for [time, i, j] in logs:
            if (i,j) not in logsmap.keys() and (j,i) not in logsmap.keys():
                logsmap[(i,j)] = time
            else:
                if (i,j) in logsmap.keys():
                    logsmap[(i,j)] = min(time, logsmap[(i,j)])
                else:
                    logsmap[(j, i)] = min(time, logsmap[(j, i)])
        logsmap = sorted(logsmap.items(), key=lambda x:x[1])
        # print('logsmap:', logsmap)
        for ((i,j),time) in logsmap:
            if not unionset.isSameSet(i, j):
                unionset.union(i, j)
                res = max(res, time)


        if unionset.rankMap[unionset.findHead(unionset.elementMap[0])] == N:
            return res
        return -1

if __name__ == '__main__':
    # logs = [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
    #         [20190312, 1, 2], [20190322, 4, 5]]
    logs = [[3,0,3],[4,1,2],[0,2,0],[2,0,2],[8,0,3],[1,0,1],[5,1,2],[7,3,1],[6,1,0],[9,3,0]]
    # N = 6
    N = 4
    S = Solution()
    print(S.earliestAcq(logs,N))
