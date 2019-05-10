# -*- coding: utf-8 -*-
# @Date    : 2019/4/20
# @Time    : 18:44
# @Author  : Daishijun
# @File    : statisticString.py
# Software : PyCharm
'''
字符串的统计字符串
'''

def getCountString(string):
    if not string:
        return ''
    res = string[0]
    num =1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            num +=1
        else:
            res = res + '_'+str(num)+'_'+string[i]
            num = 1
    return res+'_'+str(num)

'''给第一个字符串的统计字符串，再给一个整数index，返回统计字符串代表的原字符串上index位置上的字符
'''
def getCharAt(cstr, index):
    if not cstr:
        return 0
    stage = True
    cur = ''
    num = 0
    ssum = 0
    for i in range(len(cstr)):
        if cstr[i] == '_':
            stage = not stage
        elif stage:
            ssum +=num
            if ssum > index:
                return cur
            num = 0
            cur = cstr[i]
        else:
            num = num*10+ord(cstr[i])-ord('0')
    ssum = ssum*10 + ord(cstr[i])-ord('0')
    if ssum>index:
        return cur
    else:
        return 0




if __name__ == '__main__':
    string = 'aaabbadddffc'
    print(getCountString(string))

    cstr = getCountString(string)

    print(getCharAt(cstr, 3))
