# -*- coding: utf-8 -*-
# @Date    : 2019/6/2
# @Time    : 15:04
# @Author  : Daishijun
# @File    : NQueens.py
# Software : PyCharm

'''N皇后问题'''

def isValid(record, index, j):
    for k in range(0, index):
        if j== record[k] or (abs(k-index) == abs(j - record[k])):
            return False
    return True


def process1(index,record, n):
    '''

    :param index:    摆放第index行的皇后
    :param record:
    :param n:
    :return:
    '''
    if index == n:
        return 1
    res = 0
    for j in range(0, n):
        if isValid(record, index, j):
            record[index] = j
            res += process1(index+1, record, n)
    return res


def num1(n):
    if n<1:
        return 0
    record = [0 for i in range(n)]    #记录第i行的棋子放在第几列
    return process1(0, record, n)


'''位运算符的方式对于python而言有问题，因为并没有固定表示位数。   对于这道题来说好像没有问题，、
甚至没有必须保证在32皇后以下的限制'''
def intToBin32(num):
    return (bin(((1<<32)-1)&num)[2:]).zfill(32)

def process2(upperLim, colLim, leftDiaLim, rightDialLim):
    '''

    :param upperLim:     递归过程中不变的量，表示可以放置棋子的列
    :param colLim:     递归到上一行为止，已经有哪些列上被放了棋子
    :param leftDiaLim:     由于已经放置的所有棋子，导致左下方为止不能放棋子的位置：1==》不能放
    :param rightDialLim:   类似，右下方不能放棋子的位置
    :return:     剩余的棋子， 在已经之前棋子的影响下，有多少中放置方法。
    '''
    if colLim == upperLim:   #全部放好了
        return 1
    pos = upperLim & (~(colLim | leftDiaLim | rightDialLim))    #当前行可以放置的位置
    res = 0
    while pos :
        mostRightOne = pos &(~pos+1)    #位运算快速找到最右侧的1
        pos -= mostRightOne
        res += process2(upperLim, colLim|mostRightOne, (leftDiaLim|mostRightOne)<<1, (rightDialLim|mostRightOne)>>1)
    return res

def num2(n):
    upperLim = (1<<n)-1
    return process2(upperLim, 0, 0 ,0)




if __name__ =='__main__':
    print(intToBin32(-1))
    print(num2(33))

