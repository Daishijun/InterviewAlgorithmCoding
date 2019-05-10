# -*- coding: utf-8 -*-
# @Date    : 2019/3/31
# @Time    : 14:40
# @Author  : Daishijun
# @File    : unionfind.py
# Software : PyCharm

class Element():
    def __init__(self, value):
        self.val = value

class UnionFindSet():
    def __init__(self, ls):
        self.elementdict = {}
        self.fatherdict = {}
        self.rankdict = {}
        for val in ls:
            element = Element(val)
            self.elementdict[val] = element
            self.fatherdict[element] = element
            self.rankdict[element] = 1
    def findHead(self, ele):
        path = []
        while(ele != self.fatherdict.get(ele)):
            path.append(ele)
            ele = self.fatherdict.get(ele)
        while len(path):
            self.fatherdict[path.pop()] = ele
        return ele

    def isSameSet(self, vala, valb):
        if vala in self.elementdict.keys() and valb in self.elementdict.keys():
            return self.findHead(self.elementdict[vala])==self.findHead(self.elementdict[valb])
        else:
            return False
    def union(self, vala, valb):
        if vala in self.elementdict.keys() and valb in self.elementdict.keys():
            aF = self.findHead(self.elementdict[vala])
            bF = self.findHead(self.elementdict[valb])
            if aF!=bF :
                big = aF if self.rankdict[aF] > self.rankdict[bF] else bF
                small = bF if big==aF else aF
                self.fatherdict[small] = big
                self.rankdict[big] = self.rankdict[small] + self.rankdict[big]
                self.rankdict.pop(small)

if __name__ == '__main__':
    lis = [1,2,3,4,5,6,7,8,9]
    unset = UnionFindSet(lis)
    print(unset.isSameSet(1,3))

    unset.union(1,2)
    unset.union(3,4)
    unset.union(5,4)
    unset.union(1,4)
    print(unset.isSameSet(2,3))
    print(unset.rankdict)
