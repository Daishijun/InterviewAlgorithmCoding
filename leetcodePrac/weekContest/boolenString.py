#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/30 11:46
# @Author   : Daishijun
# @Site     : 
# @File     : boolenString.py
# @Software : PyCharm


'''布尔表达式'''

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack1 = []
        symstack2 = []
        opsdict = {'|', '&','!'}
        for char in expression:
            if char == ',':
                continue
            elif char in opsdict:
                symstack2.append(char)
            elif char == 't':
                stack1.append(True)
            elif char == 'f':
                stack1.append(False)
            elif char == '(':
                stack1.append(char)
            else:
                op = symstack2.pop()
                tmp = stack1[-1]

                while stack1 and stack1[-1] != '(':
                    print('stack:', stack1)
                    if op == '|':
                        tmp = stack1.pop() or tmp   #这里可以换成|， 下面的and可以换成&， 这样可以绕开短路效应。
                    elif op == '&':
                        tmp =  stack1.pop() and tmp
                        print('tmp:', tmp)
                    else:
                        tmp = not stack1.pop()

                stack1.pop()
                stack1.append(tmp)
        return stack1[0]

if __name__ == '__main__':
    S = Solution()
    exp = "&(t,f)"
    print(S.parseBoolExpr(exp))

    print('a'.isnumeric())
