#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/7 11:49
# @Author   : Daishijun
# @Site     : 
# @File     :
# @Software : PyCharm

'''LeetCode周赛 题四  有效括号的嵌套深度'''


class Solution:
    def maxDepthAfterSplit(self, seq: str):
        res = [0]*len(seq)
        if not seq or seq == '':
            return []
        Anum = 0
        Bnum = 0
        for i in range(len(seq)):
            if seq[i] == '(':
                if Anum <= Bnum:
                    res[i] = 0
                    Anum +=1
                else:
                    res[i] = 1
                    Bnum +=1
            else:
                if Anum<= Bnum:
                    res[i] = 1
                    Bnum -=1
                else:
                    res[i] =0
                    Anum -=1
        return res

if __name__ == '__main__':
    S = Solution()
    # seq = "()(())()"
    seq = "(((())))(((())))"
    print(S.maxDepthAfterSplit(seq))