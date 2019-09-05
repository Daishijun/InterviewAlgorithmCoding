#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/9/1 11:04
# @Author   : Daishijun
# @Site     : 
# @File     : p2.py
# @Software : PyCharm

class Solution:
    def dietPlanPerformance(self, calories, k: int, lower: int, upper: int) -> int:
        res = 0
        for i in range(0,len(calories)-k+1, 1):
            tmpsum = sum(calories[i:i+k])
            print('tmpsum:',tmpsum)
            if tmpsum>upper:
                res +=1
            elif tmpsum<lower:
                res -=1
            else:
                pass
        return res
if __name__ == '__main__':
    S = Solution()

    lis = [6,13,8,7,10,1,12,11]
    k = 6
    lower = 5
    upper = 37
    print(S.dietPlanPerformance(lis,k,lower,upper))