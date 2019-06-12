# -*- coding: utf-8 -*-
# @Date    : 2019/6/2
# @Time    : 12:24
# @Author  : Daishijun
# @File    : expressionMakeupMethods.py
# Software : PyCharm

'''表达式得到期望结果的组成种数'''
'''
每一步有两个分支：需要记录每一部分为True的个数，为False的个数，所以需要两个矩阵来分别记录
'''


def isValid(express):
    if len(express)&1 == 0:
        return False
    for i in range(0, len(express), 2):
        if (express[i] != '0') and (express[i] !='1'):
            return False
    for i in range(1, len(express), 2):
        if (express[i] != '&') and (express[i] != '|') and (express[i] !='^'):
            return False
    return True

def num2(exp, desire):
    if not exp or exp == '':
        return 0
    if not isValid(exp):
        return 0

    tmat = [[0 for j in range(len(exp))] for i in range(len(exp))]
    fmat = [[0 for j in range(len(exp))] for i in range(len(exp))]

    tmat[0][0] = 0 if exp[0]=='0' else 1
    fmat[0][0] = 1 if exp[0]=='0' else 0

    for i in range(2, len(exp), 2):    #i总是指向数字位置,0或者1
        tmat[i][i] = 0 if exp[0]=='0' else 1
        fmat[i][i] = 1 if exp[0]=='0' else 0
        for j in range(i-2, -1, -2):
            for k in range(j,i, 2):
                if exp[k+1] == '&':
                    tmat[j][i] += tmat[j][k]*tmat[k+2][i]
                    fmat[j][i] += (tmat[j][k]+fmat[j][k])*fmat[k+2][i] + fmat[j][k]*tmat[k+2][i]
                elif exp[k+1] == '|':
                    tmat[j][i] += tmat[j][k]*tmat[k+2][i]+tmat[j][k]*fmat[k+2][i]+fmat[j][k]*tmat[k+2][i]
                    fmat[j][i] += fmat[j][k] * fmat[k+2][i]
                else:
                    tmat[j][i] +=fmat[j][k]*tmat[k+2][i] + tmat[j][k]*fmat[k+2][i]
                    fmat[j][i] +=tmat[j][k]*tmat[k+2][i] + fmat[j][k]*tmat[k+2][i]
    return tmat[0][len(exp)-1] if desire else fmat[0][len(exp)-1]

if __name__ == '__main__':
    exp = '1^0|0|1'
    print(num2(exp, False))