# -*- coding: utf-8 -*-
# @Date    : 2019/4/7
# @Time    : 10:53
# @Author  : Daishijun
# @File    : numeric.py
# Software : PyCharm
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False

        def scanUint(s, index):
            indback = index
            while len(s) > 0 and index<len(s) and s[index] <= '9' and s[index] >= '0':
                index += 1
            return index > indback, index

        def scanint(s, index):
            if len(s)>index and (s[index] == '+' or s[index] == '-'):
                index += 1
            return scanUint(s, index)

        numeric, ind = scanint(s, 0)
        print('ind:', ind)
        print('numeric:', numeric)
        if ind<len(s) and s[ind] == '.':
            ind += 1
            numericB, ind = scanUint(s, ind)
            numeric = numeric or numericB
        if ind<len(s) and (s[ind] == 'e' or s[ind] == 'E'):
            ind += 1
            numericC, ind = scanint(s, ind)
            numeric = numeric and numericC
        return numeric and ind == len(s)

s = '12e'
solu = Solution()
print(solu.isNumeric(s))