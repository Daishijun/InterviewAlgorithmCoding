# -*- coding: utf-8 -*-
# @Date    : 2019/6/6
# @Time    : 14:27
# @Author  : Daishijun
# @File    : stockBestTime.py
# Software : PyCharm

'''Leetcode 309 最佳买卖股票时机 含冷冻期'''

def maxProfit(prices):
    if len(prices)<2:
        return 0
    sell = [0 for i in range(len(prices))]
    buy = [0 for i in range(len(prices))]
    cool = [0 for i in range(len(prices))]
    buy[0] = -prices[0]
    for i in range(1, len(prices)):
        sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        buy[i] = max(buy[i-1], cool[i-1]-prices[i])    #买入时候已经把成本价算进去了，所以在计算卖出时，只需要加上price[i]就行了。
        cool[i] = sell[i-1]    #每一轮更新其实只跟上一轮的值有关，可以空间压缩
    return max(sell[-1], cool[-1])

if __name__ == '__main__':
    prices = [1,2,3,0,2]
    print(maxProfit(prices))

