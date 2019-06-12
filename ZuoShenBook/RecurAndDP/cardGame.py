# -*- coding: utf-8 -*-
# @Date    : 2019/5/15
# @Time    : 9:01
# @Author  : Daishijun
# @File    : cardGame.py
# Software : PyCharm

'''
排成一条线的纸牌博弈问题
返回最后获胜者的分数
'''

def f(arr, i,j):
    if i==j:
        return arr[i]
    else:
        return max(arr[i]+s(arr,i+1,j), arr[j] + s(arr, i, j-1))

def s(arr, i, j):
    if i==j:
        return 0
    else:
        return min(f(arr,i+1, j), f(arr,i,j-1))

def win1(arr):
    if not arr:
        return 0
    return max(f(arr, 0 ,len(arr)-1), s(arr, 0, len(arr)-1))

def win2(arr):
    if not arr:
        return 0
    f = [[0 for i in range(len(arr))] for j in range(len(arr))]
    s = [[0 for i in range(len(arr))] for j in range(len(arr))]
    for j in range(len(arr)):
        f[j][j] = arr[j]
        for i in range(j-1, -1, -1):
            f[i][j] = max(arr[i]+s[i+1][j], arr[j]+s[i][j-1])
            s[i][j] = min(f[i+1][j], f[i][j-1])
    return max(f[0][len(arr)-1], s[0][len(arr)-1])    #这里显式的比较一下，可以区分出是先手的胜利还是后手的胜利。

if __name__ == '__main__':
    arr = [1,2,100,4]
    print(win1(arr))
    print(win2(arr))
