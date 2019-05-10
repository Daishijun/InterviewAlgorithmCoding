# -*- coding: utf-8 -*-
# @Date    : 2019/4/24
# @Time    : 16:38
# @Author  : Daishijun
# @File    : formulaString.py
# Software : PyCharm
'''
公式字符串求值
p.s. 假设输入字符串都是合法的公式
'''

def getNum(deq):
    '''
    :param deq:     双端队列，数字和+，-号以字符串的形式，一个一个元素分开存在deq中
    :return:
    '''
    res = 0
    add = True

    while deq:
        cur = deq.pop(0)
        if cur == '+':
            add = True
        elif cur == '-':
            add = False
        else:
            num = int(cur)
            res += num if add else -num

    return res

def addNum(deq, num):
    if deq:
        top = deq.pop()
        if top == '+' or top == '-':
            deq.append(top)
        else:
            cur = int(deq.pop())
            num = num*cur if top=='*' else num//cur
    deq.append(str(num))

def value(string, ind):
    deq = []
    pre = 0
    while ind<len(string) and string[ind] !=')':
        if string[ind] >= '0' and string[ind] <='9':
            pre = pre *10 + ord(string[ind])-ord('0')
            ind +=1
        elif string[ind] !='(':
            addNum(deq, pre)
            deq.append(string[ind])
            ind +=1
            pre = 0
        else:
            bra = value(string, ind+1)
            pre = bra[0]
            ind = bra[1]+1
    addNum(deq, pre)
    return [getNum(deq), ind]

def getValue(string):
    return value(string,0)[0]

if __name__ == '__main__':
    # dep = ['1','+','5','+','6','-','1']
    # print(getNum(deq=dep))
    string = '48*((70-65)-43)+8*1'
    # print(getValue(string))
    import re
    strli = re.split('[\+|\-|\*]', string)
    print(strli)


