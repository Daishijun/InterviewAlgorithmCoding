# -*- coding: utf-8 -*-
# @Date    : 2019/4/23
# @Time    : 20:32
# @Author  : Daishijun
# @File    : meituan1.py
# Software : PyCharm
#
# rows=3
# cols=3
# arr=[[1, 1, 1], [1, 5, 1], [1, 1, 1]]


rows, cols = list(map(int, input().split()))
arr = []
for i in range(rows):
    arr.append(list(map(int, input().split())))



num_set=set()
for i in range(rows):
    for j in range(cols):
        num_set.add(arr[i][j])

def gen_chess_matrix(rows=4,cols=3,corner_color=1):
    middle_color = 1-corner_color
    dp=[]
    for i in range(rows):
        line=[]
        for j in range(cols):
            if (i+j)%2 ==0:
                line.append(corner_color)
            else:
                line.append(middle_color)
        dp.append(line)
    return dp

chess_one= gen_chess_matrix(rows, cols, 1)    #生成中心颜色为1的矩阵，角落颜色为0
chess_two= gen_chess_matrix(rows, cols, 0)    #生成中心颜色为0的矩阵
num_dict={}
ind=0
for key in num_set:
    num_dict[key]=ind
    ind+=1    #原矩阵中有多少种不同的颜色
    #  small bug ,only require two elements
def dis_of_matrix(chess_matrix,matrix,num_dict=num_dict):
    m,n=len(matrix),len(matrix[0])
    res=0
    tmp=0
    for i in range(m):
        for j in range(n):
            x= matrix[i][j]    #原来的颜色
            tmp= num_dict[x]
            res+= tmp ^ chess_matrix[i][j]
    return res
a1=dis_of_matrix(chess_one, arr)
a2=dis_of_matrix(chess_two, arr)
ans=min(a1,a2)
print(ans)