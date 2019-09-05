#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/17 20:30
# @Author   : Daishijun
# @Site     : 
# @File     : Prob2.py
# @Software : PyCharm

def process(row, col, inputmat,mat, rows, cols, targetx, targety):
    print('rows:{}, cols:{}'.format(rows, cols))
    print('start precess')
    print('mat',mat)
    if row<1 or col<1 or row>rows or col> cols or (inputmat[row-1][col-1]=='.' and mat[row][col]>1) or (inputmat[row-1][col-1]=='X' and mat[row][col]>0):
        # print('mat inner', mat)
        # print('row:{} col:{} rows:{} cols:{}\n'.format(row,col, rows, cols),row<1 , col<1 , row>rows , col>cols, (inputmat[row-1][col-1]=='.' and mat[row][col]>1) , (inputmat[row-1][col-1]=='X' and mat[row][col]>0))
        return False
    else:
        mat[row][col] +=1
        print('mat inner :', mat)
        if row == targetx and col==targety and ((inputmat[row-1][col-1]=='.' and mat[row][col]==2) or (inputmat[row-1][col-1] == 'X' and mat[row][col]==1)):
            print('row:{} col:{}    target{}{}'.format(row,col,targetx,targety))
            return True
        else:
            print('false branch')
            has =  process(row-1, col,inputmat,mat, rows, cols, targetx, targety) or process(row +1, col, inputmat, mat, rows, cols, targetx, targety) or process(row, col-1, inputmat, mat, rows, cols, targetx, targety) or process(row , col+1, inputmat, mat, rows,cols, targetx, targety)
            if not has:
                mat[row][col] -=1
            return has


def check(sx, sy,ex,ey, rows, cols, wordmat):
    row = sx-1
    col = sy-1
    if wordmat[row][col] == 'X' or (sx > 1 and sx < rows and sy<cols and sy>1) :
        return True
    else:
        if (row-1>0 and wordmat[row-1][col] == '.') or \
                (row + 1 <rows and wordmat[row + 1][col] == '.') or \
                (col - 1 > 0 and wordmat[row ][col-1] == '.') or \
                (col + 1 <cols and wordmat[row][col+1] == '.'):
            return True
        elif (row==1 or row == rows) and (col==1 or col == cols):
            return False
        elif (sy == 1 and sx == ex and ey==sy+1) or \
                (sy == cols and sx == ex and ey == sy-1) or \
                (sx == 1 and sy == ey and ex == sx + 1) or \
                (sy == rows and sx == ex and ey == sy - 1) :
            return False
        else:
            return True

if __name__ == '__main__':
    N = int(input())
    reslist = []
    for j in range(N):
        n, m = list(map(int, input().split()))

        wordmat = []
        for i in range(n):
            wordmat.append(list(input()))

        # for i in range(n):
        #     print(wordmat[i])

        sx, sy = list(map(int, input().split()))
        tx, ty = list(map(int, input().split()))
        print(wordmat[sx-1][sy-1])
        print(wordmat[tx-1][ty-1])

        # mat = [[0]*(m+1) for i in range(n+1)]
        # print('n:{}, m = {}'.format(n, m))
        if check(sx,sy,tx, ty,n,m,wordmat):
            reslist.append('YES')
            # print(mat)
        else:
            # print(mat)
            reslist.append('NO')
    for j in range(N):
        print(reslist[j])

    # wordmat = [['X','.','.','.','X','X'],
    #            ['.','.','.','X','X','.'],
    #            ['.','X','.','.','X','.'],
    #            ['.','.','.','.','.','.']]

    #
    # n = 4
    # m=6
    # mat = [[0]*(m+1) for i in range(n+1)]
    # if process(1,6,wordmat, mat,n,m,2,2):
    #     print('yes')
    #     # print(mat)
    # else:
    #     # print(mat)
    #     print('no')