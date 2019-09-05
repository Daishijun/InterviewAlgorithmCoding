#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/3 19:25
# @Author   : Daishijun
# @Site     : 
# @File     : prob1.py
# @Software : PyCharm

'''1'''

string = input()
strlist = list(string)
stack = []
count = 0
for i in range(len(strlist)):
    if strlist[i] == '<' :
        if len(stack)>0 and count==0:
            stack.pop(-1)
    elif strlist[i] == '(':
        count +=1
    elif strlist[i] == ')':
        count -=1
    else:
        if count==0:
            stack.append(strlist[i])

print(''.join(stack))