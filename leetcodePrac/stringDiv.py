#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/16 17:52
# @Author   : Daishijun
# @Site     : 
# @File     : stringDiv.py
# @Software : PyCharm

'''Leetcode 399 除法求值'''

'''
这个题的dfs有点不好写。
'''

class Solution:
    def calcEquation(self, equations ,\
                     values, queries) :
        mapdict = {}

        for (x,y), val in zip(equations, values):
            if x in mapdict.keys():
                mapdict[x][y] = val
            else:
                mapdict[x] = {y:val}
            if y in mapdict.keys():
                mapdict[y][x] = 1/val
            else:
                mapdict[y] = {x: 1/val}
        def dfs(noda1, node2):
            if noda1 not in mapdict.keys() :
                return -1
            if noda1 == node2:
                return 1
            for node in mapdict[noda1].keys():
                if node == node2:
                    return mapdict[noda1][node]
                elif node not in visited:
                    visited.add(node)
                    val = dfs(node, node2)
                    if val != -1:
                        return mapdict[noda1][node] * val
            return -1

        res = []
        for qs, qt in queries:
            visited = set()
            res.append(dfs(qs, qt))
        return res

