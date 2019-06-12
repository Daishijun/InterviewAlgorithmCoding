# -*- coding: utf-8 -*-
# @Date    : 2019/5/19
# @Time    : 14:18
# @Author  : Daishijun
# @File    : minPath.py
# Software : PyCharm

'''最短通路值'''

def walkto(pre, toR, toC, mat, mapdis, rowQ, colQ):
    if toR<0 or toR == len(mat) or toC<0 or toC==len(mat[0]) or mat[toR][toC] == 0 or mapdis[toR][toC] !=0:
        return
    mapdis[toR][toC] = pre+1
    rowQ.append(toR)
    colQ.append(toC)

def minPathValue(mat):
    if not mat or len(mat)<1 or len(mat[0])<1 or mat[0][0]==0 or mat[-1][-1] == 0:    #需要保证出发点和目的地都是1
        return 0
    res = 0
    mapdic = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
    mapdic[0][0] = 1
    rowQ = [0]
    colQ = [0]
    while rowQ:
        r = rowQ.pop(0)    #从队列头弹出
        c = colQ.pop(0)
        if r == len(mat)-1 or c == len(mat[0])-1:
            return mapdic[r][c]
        walkto(mapdic[r][c], r-1, c, mat, mapdic, rowQ,colQ)
        walkto(mapdic[r][c], r+1, c, mat, mapdic, rowQ,colQ)
        walkto(mapdic[r][c], r, c-1, mat, mapdic, rowQ,colQ)
        walkto(mapdic[r][c], r, c+1, mat, mapdic, rowQ,colQ)
    return res    #这里的res好像没什么用





