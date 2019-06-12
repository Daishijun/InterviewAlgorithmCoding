# -*- coding: utf-8 -*-
# @Date    : 2019/5/19
# @Time    : 21:56
# @Author  : Daishijun
# @File    : projectMaxProfit.py
# Software : PyCharm

'''做项目的最大收益问题'''

'''自己写的，复杂度要高于左神'''
def maxProfits(W, K, costs , profits):
    tasklist = []

    for i in range(K):
        curlist = []
        for ind in range(len(costs)):

            if costs[ind] <=W:

                curlist.append(ind)
        print('curlist:', curlist)
        if len(curlist) == 0:
            break
        maxind = curlist[0]
        for j in range(1,len(curlist)):
            maxind = curlist[j] if profits[maxind]<profits[curlist[j]] else maxind

        print('index:',maxind)
        tasklist.append(maxind)
        W += profits[maxind]
        costs.pop(maxind)
        profits.pop(maxind)
        print('costs:', costs)
        print('profits:', profits)



    print(tasklist)
    return W

if __name__ == '__main__':
    W = 3
    K =2
    costs = [5,4,1,2]
    profits = [3,5,3,2]

    print(maxProfits(W, K, costs, profits))

