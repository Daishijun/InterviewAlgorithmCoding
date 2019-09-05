#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/11 11:10
# @Author   : Daishijun
# @Site     : 
# @File     : ordinalData.py
# @Software : PyCharm

'''1'''


class Solution:
    def ordinalOfDate(self, date: str) -> int:
        monthlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.split('-'))
        #check run
        flag = False
        if year%400 == 0:
            flag = True
        elif year%100 and year%4 ==0:
            flag = True

        res = 0
        for i in range(month-1):
            res += monthlist[i]
        res += day
        if month>2 and flag:
            res += 1
        return res