# -*- coding: utf-8 -*-
# @Date    : 2019/6/2
# @Time    : 11:00
# @Author  : Daishijun
# @File    : numStringToLetter.py
# Software : PyCharm

'''数字字符串转换为字母组合的种数'''
'''
与剑指的题不用，这里1--》A； 26-->Z;
剑指：0--》A； 25--》Z
'''

def process(string, i):
    '''
    暴力递归
    :param string:
    :param i:
    :return: 在string[0..i-1]已经转换好的情况下，string[i,N-1]有多少种转换方式
    '''
    if i == len(string):
        return 1
    if string[i] == '0':
        return 0
    res = process(string, i+1)
    if i< len(string)-1 and ((ord(string[i]) - ord('0'))*10+(ord(string[i+1])- ord('0'))<27):
        res += process(string, i+2)
    return res

def num2(string):
    if not string or string == '':
        return 0
    cur = 0 if string[len(string)-1] == '0' else 1
    nextpos = 1 #记录p[i+2]的可能数

    for i in range(len(string)-2, -1,-1):
        if string[i] == '0':
            nextpos = cur
            cur =0     #第i位置时，因为==‘0’，所以此位置没有
        else:
            tmp = cur
            if (ord(string[i]) - ord('0'))*10+(ord(string[i+1])- ord('0'))<27:
                cur += nextpos   #cur更新为p[i]的结果
            nextpos = tmp
    return cur

if __name__ == '__main__':
    string = '1111'
    print(num2(string))


