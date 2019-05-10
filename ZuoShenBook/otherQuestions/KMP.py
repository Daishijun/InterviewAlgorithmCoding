# -*- coding: utf-8 -*-
# @Date    : 2019/5/10
# @Time    : 9:22
# @Author  : Daishijun
# @File    : KMP.py
# Software : PyCharm

'''
KMP 算法， 包含子串问题：如果strz中含有子串match,则返回match在str中的开始位置， 不包含就返回-1.
'''

#获得match串的nextArr
def getNextArr(match):
    if len(match)==1:
        return -1
    nextArr = [0 for i in range(len(match))]
    nextArr[0] = -1
    nextArr[1] = 0
    pos = 2    #要计算的nextArr[]的位置
    cn = 0    #cn表示的是要与pos位置比较的位置，也可以表示最长的匹配长度
    while pos< len(nextArr):
        if match[pos-1] == match[cn]:
            nextArr[pos]  = cn+1
            pos +=1
            cn +=1
        elif cn>0:
            cn = nextArr[cn]    #向前找
        else:    #已经找到nextArr[0]了，说明没有匹配的
            nextArr[pos] = 0
    return nextArr


#主体
def getIndexOf(string, match):
    if not string or not match or len(string)==0 or len(match)==0:
        return -1
    nextArr = getNextArr(match)    #获得match的nextArr数组
    si = 0    #待匹配的string的下标
    mi = 0
    while si<len(string) and mi<len(match):
        if string[si] == match[mi]:
            si +=1
            mi +=1
        elif nextArr[mi] == -1:
            si +=1
        else:
            mi = nextArr[mi]
    res = -1
    if mi == len(match):
        res = si-mi
    return res


if __name__ == '__main__':
    string = 'acbc'
    match = 'bc'
    print(getIndexOf(string, match))

