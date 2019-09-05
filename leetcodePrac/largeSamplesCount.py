#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/6/23 10:34
# @Author   : Daishijun
# @Site     : 
# @File     : largeSamplesCount.py
# @Software : PyCharm

'''Leetcode 1093 '''


class Solution:
    def sampleStats(self, count) :
        if count == [] or sum(count) == 0:
            return [0.0,0.0,0.0,0.0,0.0]
        valsum = 0
        for i in range(len(count)):
            if count[i] !=0:
                small = i *1.0
                break
        for j in range(len(count)-1, -1, -1):
            if count[j] !=0:
                large = j *1.0
                break

        numcount = sum(count)  #总共的数字个数
        numcur = 0
        oddflag = numcount&1    #奇数个为1
        mid = 0
        mid1 =-1
        for ind, val in enumerate(count):
            numcur += val
            if oddflag and numcur>=(numcount+1)//2:
                mid = ind *1.0
                break
            else:
                if numcur == (numcount+1)//2:
                    mid1 = ind
                if numcur > (numcount+1) //2:
                    if mid1 ==-1:
                        mid = ind *1.0
                    else:
                        mid = (ind+mid1)/2.0
                    break

        for ind, val in enumerate(count):
            valsum += ind*val

        avg = valsum/numcount

        zhongshu = count.index(max(count)) *1.0
        return [small, large, avg, mid, zhongshu]

if __name__ == '__main__':
    S = Solution()
    count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    print(S.sampleStats(count))