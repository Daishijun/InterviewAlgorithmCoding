#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/5 11:09
# @Author   : Daishijun
# @Site     : 
# @File     : reverseSubstring.py
# @Software : PyCharm

'''翻转字符串'''

'''
    整体翻转，部分翻转
'''

'''
记录下补充问题，部分旋转，即前k个字符放到最后去。
方法一：也可以用部分翻转+整体翻转的思路
方法二：分左右部分，字符数少的部分交换后不在变化，直到左右部分长度相等，则交换之后结束。
最多发生N次交换。
'''

def exchange(chas, start, end, size):
    i = end-size+1

    while size>0:
        tmp = chas[start]
        chas[start] = chas[i]
        chas[i] = tmp
        size -=1
        start +=1
        i+=1
    #也可以直接
    #chas[start:start+size], chas[i:end+1] = chas[i:end+1], chas[start:start+size]


def rotate2(chas, size):
    if not chas or size<=0 or size >= len(chas):
        return
    start = 0
    end = len(chas)-1
    lpart = size
    rpart = len(chas) - size
    solid = min(lpart, rpart)
    diff = lpart - rpart
    while 1:
        exchange(chas, start, end, solid)
        if diff == 0:
            break
        elif diff>0:
            start += solid
            lpart = diff
        else:
            end -= solid
            rpart = -diff
        solid = min(lpart, rpart)
        diff = lpart- rpart

if __name__== '__main__':
    string = '1234567ABCD'
    strlist = list(string)
    size = 7
    rotate2(strlist, size)
    print(strlist)