#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/16 17:13
# @Author   : Daishijun
# @Site     : 
# @File     : searchInMat.py
# @Software : PyCharm

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or matrix== [] or matrix[0] == []:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        i = 0
        j = cols-1
        while i<rows and j>-1:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -=1
            else :
                i +=1
        return False