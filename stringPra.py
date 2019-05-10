# -*- coding: utf-8 -*-
# @Date    : 2019/4/6
# @Time    : 23:24
# @Author  : Daishijun
# @File    : stringPra.py
# Software : PyCharm

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s == None or pattern == None:
            return False

        def Core(s, pat):
            if len(s) == 0 and len(pat) == 0:
                return True
            if len(pat) == 0 and len(s) > 0:
                return False
            if len(s) == 0 and len(pat) < 2:
                return False
            else:
                if len(s) > 0  :
                    if len(pat)>1 and pat[1] == '*':

                        if pat[0] == '.' or pat[0] == s[0]:
                            return Core(s[1:], pat[2:]) or Core(s[1:], pat[:]) or Core(s[:], pat[2:])
                        else:
                            return Core(s[:], pat[2:])
                    elif (pat[0] == '.' or s[0] == pat[0]):
                        return Core(s[1:], pat[1:])
                else:
                    if  len(pat)>1 and  pat[1] == '*':
                        return Core(s[:], pat[2:])
            return False

        return Core(s, pattern)

Ss = Solution()
s = 'a'
patt = '.'
print(Ss.match(s, patt))

