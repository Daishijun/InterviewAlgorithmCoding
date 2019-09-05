#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/7 10:27
# @Author   : Daishijun
# @Site     : 
# @File     :
# @Software : PyCharm

'''Leetcode 周赛题一 IP地址无效化'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ''
        for s in address:
            if s == '.':
                res += '[.]'
            else:
                res += s
        return res

if __name__ == '__main__':
    # address = "1.1.1.1"
    address = "255.100.50.0"
    S = Solution()
    print(S.defangIPaddr(address))

    
