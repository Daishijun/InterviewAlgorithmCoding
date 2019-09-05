#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/3 18:56
# @Author   : Daishijun
# @Site     : 
# @File     : beibao01.py
# @Software : PyCharm

def dp(weight, count, weights, costs):
    """
    动态规划模板，时间复杂度O(weight * count), 空间复杂度O(weight)
    :param weight: 背包最大能装的重量
    :param count: 物品数量
    :param weights: 每件物品的重量
    :param costs: 每件物品的价值
    :return: 背包装下的最大价值
    """
    preline, curline = [0] * (weight + 1), [0] * (weight + 1)
    for i in range(count):
        for j in range(weight + 1):
            if weights[i] <= j:
                curline[j] = max(preline[j], costs[i] + preline[j - weights[i]])
        preline = curline[:]
    return curline[weight]


# count：物品数量； weight：背包总重量； costs： 每件物品的价值； weight：每件物品的重量
count, weight = 5, 10
costs = [200, 300, 350, 400, 500]
weights = [3, 4, 3, 5, 5]
print(dp(weight, count, weights, costs))
