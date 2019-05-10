# -*- coding: utf-8 -*-
# @Date    : 2019/4/23
# @Time    : 21:14
# @Author  : Daishijun
# @File    : meituan3.py
# Software : PyCharm

n = 3
list1 = [1,2,3,2]
list2 = [2,5,2,3]
list3 = [1,4,3,4]

import numpy
def getAll(list1):
    dic = []
    if list1[0] == list1[2]:
        if list1[1] <= list1[3]:
            for i in range(list1[1],list1[3]+1):
                dic.append([i,list1[0]])
        else:
            for i in range(list1[3],list1[1]+1):
                dic.append([list1[0],i])

    if list1[1] == list1[3]:
        if list1[0] <= list1[2]:
            for i in range(list1[0],list1[2]+1):
                dic.append([i,list1[1]])
        else:
            for i in range(list1[2],list1[0]+1):
                dic.append([list[1],i])
    return (dic)

a = getAll(list1)
b = getAll(list2)
c = getAll(list3)

result = numpy.vstack((a,b,c))
print(result)