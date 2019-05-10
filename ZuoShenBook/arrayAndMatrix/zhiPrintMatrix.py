# -*- coding: utf-8 -*-
# @Date    : 2019/4/30
# @Time    : 16:40
# @Author  : Daishijun
# @File    : zhiPrintMatrix.py
# Software : PyCharm

'''
之字形打印矩阵
'''
def printSlash(mat, startR, startC, endR, endC, up2down):
    if up2down:
        while startR <=endR:
            print(mat[startR][startC], end=' ')
            startR +=1
            startC -=1
    else:
        while endR >= startR:
            # print('endR:',endR, 'endC:',endC)
            print(mat[endR][endC], end=' ')
            endR -=1
            endC +=1

def printMatrixZigZag(mat):
    startR_toRow, startC_toRow = 0, 0
    startR_toCol, startC_toCow = 0 ,0

    endR, endC = len(mat)-1, len(mat[0])-1
    up2down = False
    while startR_toRow <= endR:
        printSlash(mat, startR_toRow, startC_toRow, startR_toCol, startC_toCow, up2down)
        startR_toRow = startR_toRow if startC_toRow!=endC else startR_toRow+1      #！！！因为上坐标转向的标准是上坐标的纵坐标，应该放在较后更改，不然可能会漏过转折点
        startC_toRow = startC_toRow+1 if startC_toRow !=endC else startC_toRow

        startC_toCow = startC_toCow if startR_toCol != endR else startC_toCow + 1    #!!!因为下坐标转向的标准是下坐标的横坐标，应该放在较后更改。
        startR_toCol = startR_toCol+1 if startR_toCol!= endR else startR_toCol

        up2down = not up2down
        # print('上坐标：{};   下坐标：{}'.format((startR_toRow, startC_toRow), (startR_toCol, startC_toCow)))
    print('over')

if __name__ == '__main__':
    mat = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]
    printMatrixZigZag(mat)