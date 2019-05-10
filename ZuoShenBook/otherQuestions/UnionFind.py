# -*- coding: utf-8 -*-
# @Date    : 2019/5/7
# @Time    : 13:51
# @Author  : Daishijun
# @File    : UnionFind.py
# Software : PyCharm

'''
并查集结构的实现,    不包含重复值
'''

class Element():    #封装下节点
    check = 7
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


if __name__ =='__main__':
    vallist = [1.2,3,4,5,6,7]
    unionfindset = UnionFindSet(vallist)

    import numpy as np

    xlist = [[[1,2,3],[4,5,6],[7,8,9]],[[9,6,7],[3,6,4],[1,7,2]]]
    xarray = np.array(xlist)
    print(xarray)
    print('###\n',xarray[:,:,1])
    print('###\n',xarray[...,1])
    print('###\n',xarray[0,...,1])
    print('###\n',xarray[0,:,1])


