# -*- coding: utf-8 -*-
# @Date    : 2019/6/11
# @Time    : 12:25
# @Author  : Daishijun
# @File    : Manacher.py
# Software : PyCharm

'''Manacher算法，返回str中最长回文子串长度'''
'''
在线性时间内找到最长回文子串
'''

def manacherString(string):
    res = ['' for i in range(len(string)*2+1)]
    index = 0
    for i in range(len(res)):
        if i &1:
            res[i] = string[index]
            index +=1
        else:
            res[i] = '#'
    return res

def maxLcpsLength(string):
    if not string or len(string) == 0:
        return 0
    manacherlist = manacherString(string)
    pArr = [1 for i in range(len(manacherlist))]
    index = -1
    pR = -1
    maxrediu = 0
    for i in range(len(manacherlist)):
        pArr[i] = max(pArr[2*index-i], pR-i) if pR > i else 1
        while i-pArr[i]>-1 and i+pArr[i] < len(manacherlist):
            if manacherlist[i-pArr[i]] == manacherlist[i+pArr[i]]:
                pArr[i] +=1
            else:
                break
        if i+pArr[i] > pR:
            pR = i+pArr[i]
            index = i
        maxrediu = max(maxrediu, pArr[i])
    return maxrediu-1

if __name__ == '__main__':
    string = 'abc1234321ab'
    print(maxLcpsLength(string))

