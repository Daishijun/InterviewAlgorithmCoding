# -*- coding: utf-8 -*-
# @Date    : 2019/5/26
# @Time    : 17:00
# @Author  : Daishijun
# @File    : RoundC_1.py
# Software : PyCharm

def process2(R,C, SR, SC, string):
    poslist = [[SR, SC]]
    ir = SR
    ic = SC

    for s in string:
        if s=='N':
            while [ir, ic] in poslist:
                ir -=1
            poslist.append([ir, ic])

        elif s=='S':
            while [ir, ic] in poslist:
                ir +=1
            poslist.append([ir, ic])
        elif s == 'W':
            while [ir, ic] in poslist:
                ic -=1
            poslist.append([ir, ic])
        else:
            while [ir, ic] in poslist:
                ic +=1
            poslist.append([ir, ic])
    return poslist[-1]



T = int(input())
results = []
for i in range(T):

    N, R, C, SR, SC  = list(map(int, input().split()))
    string = input()

    results.append(process2(R,C, SR, SC, string))


for i in range(T):
    print('Case #{}: {} {}'.format(i+1, results[i][0], results[i][1]))

# def process(R,C, SR, SC, string):
#     grid = [[0 for i in range(C+1)] for j in range(R+1)]
#     grid[SR][SC] = 1
#     ir = SR
#     ic = SC
#
#     for s in string:
#         if s=='N':
#             while grid[ir][ic] ==1:
#                 ir -=1
#             grid[ir][ic] =1
#
#         elif s=='S':
#             while grid[ir][ic] ==1:
#                 ir +=1
#             grid[ir][ic] =1
#         elif s == 'W':
#             while grid[ir][ic] ==1:
#                 ic -=1
#             grid[ir][ic] =1
#         else:
#             while grid[ir][ic] ==1:
#                 ic +=1
#             grid[ir][ic] =1
#     return [ir, ic]
