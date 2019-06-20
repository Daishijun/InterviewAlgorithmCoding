#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/17 10:09
# @Author   : Daishijun
# @Site     : 
# @File     : stringDecode.py
# @Software : PyCharm

'''Leetcode 394 字符串解码'''

'''
两个stack，
1个用来记录重复次数，
1个用来每个次数之前的字符串，
ss用来缓存当前stack1中的数字对应的字符串,[]中的字符串

两个栈的入栈时机是==》遇到[,即数字部分终止。
'''

class Solution:
    def decodeString(self, s: str) -> str:
        stack1 = []
        stack2 = []
        ss = ''
        length = len(s)
        ind = 0
        while ind< length:
            cur = s[ind]
            if cur.isnumeric():
                hpos = ind
                while cur.isnumeric():    #这里遇到数字会一直+1， 知道cur == ‘[’的时候才跳出，此时无法进入elif 和 else, 直接跳过这个[
                    ind +=1
                    cur = s[ind]
                stack1.append(int(s[hpos:ind]))
                stack2.append(ss)    #把数字前面一段的缓存字符串入栈了，清空ss缓存。
                ss = ''
            elif cur == ']':    #遇到]开始出栈计算字符串
                ss = stack2.pop() + ss* stack1.pop()
            else:
                ss += cur
            ind +=1
        return ss


'''
用一个stack，遇到]前单纯将遍历的字符入栈，遇到后说明前面应该是有一段字母串，然后有[，然后是数字，
这里就把遇到的]对应的内容搞定了。
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        for ss in s:
            if ss != ']':
                stack.append(ss)
            else:
                string = ''
                while not stack[-1].isnumeric():    #找到数字前的串，这里会包括[符号
                    string  = stack.pop() + string
                time = ''
                while stack and stack[-1].isnumeric():
                    time = stack.pop() + time
                if time != '':
                    string = string[1:] * int(time)    #这里把[符号除去.
                if stack:
                    stack.append(string)
                else:
                    res = res + string
        return res + ''.join(stack)




if __name__ == '__main__':
    s = "3[a2[c]]"
    # S = Solution()
    # print(S.decodeString(s))
    import tensorflow as tf
    print(tf.keras.__version__)
    import keras
    print(keras.__version__)