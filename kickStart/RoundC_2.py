# -*- coding: utf-8 -*-
# @Date    : 2019/5/26
# @Time    : 17:57
# @Author  : Daishijun
# @File    : RoundC_2.py
# Software : PyCharm

# def process2(matrix, K):
#     '''
#     here K = 0
#     :param matrix:
#     :param K:
#     :return:
#     '''
#     edgelist = []
#     # maxpoint = 0
#     for line in matrix:
#         start = 0
#         edgeli = []
#         while start < len(line):
#             i = start+1
#             while i<len(line) and line[start] == line[i]:
#                 i +=1
#
#             edgeli.append([start, i-1])
#             start = i
#         edgelist.append(edgeli)
#     return edgelist

def inter(p1, p2):
    left = max(p1[0],p2[0])
    right = min(p1[1], p2[1])
    # if left<=right:
    return [left, right]
    # else:
    #     return p2

def process3(matrix, K):
    '''
    here K = 0
    :param matrix:
    :param K:
    :return:
    '''
    edgelist = []
    maxpoint = 0
    prelist = []
    for lineind in range(len(matrix)):
        # print('line:', lineind)
        start = 0
        edgeli = []

        while start < len(matrix[lineind]):
            i = start + 1
            while i < len(matrix[lineind]) and matrix[lineind][start] == matrix[lineind][i]:
                i += 1

            if prelist == []:
                edgeli.append([start, i - 1])
                maxpoint = max(maxpoint, i-start)
                # print('max:', maxpoint, '\tblock:',[start, i - 1], '\tlevel:',lineind, 'prelist is None')
                start = i

            else:
                for pre in prelist:
                    if start in list(range(pre[0],pre[1]+1)) or i-1 in list(range(pre[0],pre[1]+1)):
                        point = inter(pre,[start, i-1])
                        edgeli.append(point)
                        maxpoint = max(maxpoint, (point[1]-point[0]+1)*(lineind+1))
                        # print('max:', maxpoint,'\tblock:',point,'\tlevel:',lineind)
                start = i
        prelist = edgeli.copy()

        # edgelist.append(edgeli)
    return maxpoint

T = int(input())
results = []
for i in range(T):

    R,C,K  = list(map(int, input().split()))
    matric = []
    for j in range(R):
        matric.append(list(map(int, input().split())))


    results.append(process3(matric, K))


for i in range(T):
    print('Case #{}: {}'.format(i+1, results[i]))