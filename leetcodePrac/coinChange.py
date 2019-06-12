# -*- coding: utf-8 -*-
# @Date    : 2019/6/5
# @Time    : 19:17
# @Author  : Daishijun
# @File    : coinChange.py
# Software : PyCharm

'''Leetcode 322 零钱兑换'''

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount<0 or not coins:
            return -1
        if amount == 0:
            return 0
        def process(coins, index, rest):
            if index == len(coins):
                return 0 if rest == 0 else -1
            k = 0
            res = -1
            while k*coins[index]<=rest:
                nextres = process(coins, index+1, rest- k*coins[index])
                if nextres != -1:
                    res =nextres+ k if res == -1 else min(nextres+k, res)
                k +=1
            return res
        return process(coins, 0, amount)

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount<0 or not coins:
            return -1
        if amount == 0:
            return 0
        dp = [[-1 for i in range(amount+1)] for j in range(len(coins)+1)]
        dp[len(coins)][0] = 0
        for i in range(len(coins)-1, -1, -1):
            for j in range(amount+1):
                if dp[i+1][j] != -1:
                    dp[i][j] = dp[i+1][j]
                if j-coins[i] >-1 and dp[i][j-coins[i]] != -1:
                    if dp[i][j] == -1:
                        dp[i][j] = dp[i][j-coins[i]] +1
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][j-coins[i]]+1)
        return dp[0][amount]

if __name__ == '__main__':
    coins = [473,490,320,386,258,113,33,456,231]
    amount = 704
    s = Solution()
    print(s.coinChange(coins, amount))
