#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/23 14:56
# @Author   : Daishijun
# @Site     : 
# @File     : minPresentation.py
# @Software : PyCharm

'''最小表示法'''
'''
    求与某个字符串循环同构的所有字符串中，字典序最小的是哪个
    就是以原串不同位置的字符作为开头的旋转字符串，哪个字典序最小
    https://www.cnblogs.com/eternhope/p/9972846.html
'''

def getminInd(string):
    i = 0
    j = 1
    k = 0
    n = len(string)
    while i<n and j < n and k<n:
        diff = ord(string[(i+k)%n]) - ord(string[(j+k)%n])
        if diff == 0:
            k +=1
        else:
            if diff>0:
                i += (k+1)
            else:
                j += (k+1)
            if i == j:
                j +=1
            k = 0
    return i if i<j else j


if __name__ == '__main__':
    s = 'jdrakioi'
    print(getminInd(s))
