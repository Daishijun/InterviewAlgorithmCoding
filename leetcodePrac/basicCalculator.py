#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/1 14:53
# @Author   : Daishijun
# @Site     : 
# @File     : basicCalculator.py
# @Software : PyCharm

'''Leetcode 224 基本计算器'''

'''
原始思路：
numstack用于记录数字和'('
需要把连续的数字字符记录成一个元素，所以在连续遇到数字字符的时候需要一个tmp字符串记录，
遇到'+'，'-'的时候和遇到‘)’的时候将tmp压入numstack
opstack用于记录‘+’， ‘-’
在遇到')'时开始计算括号内的数值

！！！弹出num1, op1,将根据op1来确定num1是否取相反数。即一个数字与它前一个的符号作为一个整体。
在没有符号的情况下视为'+'
'''
class Solution:
    def calculate(self, s: str) -> int:
        numstack = []
        opstack = []
        opdict = {'+', '-'}
        numtmp = ''
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            elif s[i] in opdict:
                opstack.append(s[i])
                if numtmp != '':
                    numstack.append(numtmp)
                    numtmp = ''
            elif s[i] == ')':
                if numtmp != '':
                    numstack.append(numtmp)
                    numtmp = ''

                num1 = int(numstack.pop())
                tmp = numstack[-1]
                if tmp != '(':
                    op1 = opstack.pop()
                    if op1 == '+':
                        pass
                    else:
                        num1 = -num1
                while tmp != '(':

                    # print('nums:', numstack)

                    num2 = int(numstack.pop())
                    tmp = numstack[-1]
                    if tmp != '(':
                        op = opstack.pop()
                    else:
                        op = '+'

                    if op == '+':
                        num1 = num1 + num2
                    elif op == '-':
                        num1 = num1 - num2
                    # print('add process:', 'a=',num2, op, 'tmpres=',num1)
                numstack.pop()
                numstack.append(num1)
                # print('chuli :', numstack)
            else:
                if s[i] == '(':
                    numstack.append(s[i])
                else:
                    numtmp = numtmp + s[i]
        if numtmp != '':
            numstack.append(numtmp)
            numtmp = ''
        # print('numstack:', numstack)
        num1 = int(numstack.pop())
        op = opstack.pop() if opstack else '+'
        if op == '-':
            num1 = -num1

        while numstack:
            op = opstack.pop() if opstack else '+'
            num2 = int(numstack.pop())
            if op == '+':
                num1 = num1 + num2
            elif op == '-':
                num1 = num1 + (-num2)
        return num1

