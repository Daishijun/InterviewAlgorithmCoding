# -*- coding: utf-8 -*-
# @Date    : 2019/6/9
# @Time    : 12:13
# @Author  : Daishijun
# @File    : maxRectangle.py
# Software : PyCharm

'''Leetcode 85'''

class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        nums = [int(''.join(row), base=2) for row in matrix]

        ans, N = 0, len(nums)
        for i in range(N):
            j, num = i, nums[i]
            while j < N:    #以i行开头的矩形，最大的面积是多少，j表示层数
                num = num & nums[j]
                print('i:{}, j:{}, num:{}'.format(i, j, bin(num)))
                if not num:
                    break
                l, curnum = 0, num
                while curnum:
                    l += 1    #宽度
                    curnum = curnum & (curnum << 1)    #移位求出最大宽度
                    print('l:{},  curnum:{}'.format(l, bin(curnum)))
                ans = max(ans, l * (j-i+1))
                print('ans:{}\n'.format(ans))
                j += 1
        return ans

if __name__ == '__main__':
    matrix = [['1','0','1','0','0'],['1','0','1','1','1'],
              ['1','1','1','1','1'],['1','0','0','1','0']]
    S = Solution()
    print(S.maximalRectangle(matrix))