# -*- coding: utf-8 -*-
# @Date    : 2018/6/14
# @Time    : 14:10
# @Author  : Daishijun
# @File    : validparentheses.py
# Software : PyCharm
#
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         length = len(s)
#         arr = []
#         for i in range(length):
#             if s[i] in [')', ']', '}']:
#                 if len(arr) == 0: return False
#                 minus = abs(ord(s[i]) - ord(arr.pop()))
#                 if minus>2:
#                     return False
#             else:
#                 arr.append(s[i])
#         if len(arr) == 0 :return False
#         return True


class Solution(object):
    validin = False

    def StrToInt(self, s):
        # write code here

        if not s:
            return 0
        slen = len(s)
        num = 0
        start = 0
        minus = False
        if s[start] == '+':
            start += 1
        elif s[start] == '-':
            start += 1
            minus = True
        if slen > 1:
            num = self.Core(s[start:], minus)
        return num


    def Core(self, s, minus):
        num = 0
        ind = 0
        nlen = len(s)
        while (ind < nlen):
            print('字符：',s[ind])
            if s[ind] >= '0' and s[ind] <= '9':
                flag = -1 if minus else 1
                num = num * 10 + flag * (ord(s[ind]) - ord('0'))
                if ((minus and num < -int(0x80000000))) or (not minus and num > int(0x7FFFFFFF) ):
                    num = 0
                    break
                ind += 1
            else:
                num = 0
                break
        if ind == nlen:
            validin = True
        return num

if __name__ =='__main__':
    # s = '()[]{][)'
    # valid = Solution()
    # print(valid.isValid(s))
    s = Solution()
    ss = '++15'
    print(s.StrToInt(ss))


