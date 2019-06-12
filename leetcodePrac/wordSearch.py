# -*- coding: utf-8 -*-
# @Date    : 2019/6/10
# @Time    : 14:10
# @Author  : Daishijun
# @File    : wordSearch.py
# Software : PyCharm

'''Leetcode 79  单词搜索'''
'''
回溯法，剑指page 90
'''
class Solution:
    def exist(self, board, word: str) -> bool:
        visited = [[0 for i in range(len(board[0]))] for j in range(len(board))]

        def backtrack(row, col, curlen):
            if curlen == len(word):
                return True
            haspath = False
            if row<len(board) and row>-1 and col<len(board[0]) and col>-1 and\
                    visited[row][col] == 0 and board[row][col] == word[curlen]:
                curlen +=1
                visited[row][col] = 1
                haspath = backtrack(row-1, col, curlen) or backtrack(row+1, col, curlen) or \
                    backtrack(row, col-1, curlen) or backtrack(row, col+1, curlen)

                if not haspath:
                    curlen -=1
                    visited[row][col] = 0
            return haspath
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False


