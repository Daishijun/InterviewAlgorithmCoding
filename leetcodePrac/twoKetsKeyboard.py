#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/27 10:32
# @Author   : Daishijun
# @Site     : 
# @File     : twoKetsKeyboard.py
# @Software : PyCharm

'''Leetcode 650. 2 keys Keyboard'''

'''
思路：
因为进行复制会增加每次粘贴的字符的长度，所以应该尽可能多的进行复制。
（比如：如果只复制一次，那么每次粘贴只能增加1个字符）
如果数字n是质数，也就是说n只能被1和本身整除，那么只能1个1个粘贴；
如果是合数， 那么就可以被其他数整除，也就是说可以通过先得到除数个字符然后再复制。这里也是期望每一次复制后的粘贴步骤尽量少，
所以除数从2到n递增检查。
'''

'''
dp[i]表示要组成i个‘A’需要的最少操作步骤
如果说，存在一个可以整除i的j，即i是j的倍数，那么将dp[j]进行粘贴(i//j-1)次即可，加上1次复制，
总的操作步骤是dp[j]+i//j。
'''
class Solution:
    def minSteps(self, n: int) -> int:
        if n < 2:
            return 0
        dp = [float('inf') for i in range(n+1)]
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(dp)):
            for j in range(1,i):
                if i%j == 0:
                    dp[i] = min(dp[i], dp[j]+i//j)    #这里实际上应该把j降序选择，逆序有个贪心。
        return dp[-1]


'''
递归，有贪心，从[2,n-1）选择第一个能整除n的数字i，表示在获得n//i个连续“A”后，后续只需要i个操作即可。
对于n//i进行递归。
'''
class Solution:
    def minSteps(self, n: int) -> int:
        if n<2:
            return 0
        else:
            for i in range(2, n+1):
                if n%i == 0:
                    return self.minSteps(n//i) + i

'''
循环版本：和上面的递归相对应。
'''
class Solution:
    def minSteps(self, n: int) -> int:
        res = 0
        for i in range(2, n + 1):
            while n % i == 0:
                res += i
                n //= i

        return res
