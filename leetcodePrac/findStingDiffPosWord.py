# -*- coding: utf-8 -*-
# @Date    : 2019/6/4
# @Time    : 13:08
# @Author  : Daishijun
# @File    : findStingDiffPosWord.py
# Software : PyCharm

'''LeetCode 438 找到字符串中所有字母异位词'''



class Solution:
    def findAnagrams(self, s: str, p: str) :
        if len(s) < len(p):
            return []
        Num = []
        n = len(p)
        A = [0] * 26
        for i in range(n):
            A[ord(p[i]) - ord('a')] += 1    #要匹配的子串都加上1，
            A[ord(s[i]) - ord('a')] -= 1    #长串中的字符都减1.后续窗口移出后会加上1
        if A == [0] * 26:
            Num.append(0)
        for i in range(n, len(s)):
            A[ord(s[i]) - ord('a')] -= 1    #遍历到长串的字符。
            A[ord(s[i - n]) - ord('a')] += 1   #相当于一个长度为n的窗口，这里是把移动后滑动出去的减去。
            if A == [0] * 26:
                Num.append(i + 1 - n)
        return Num

if __name__ == '__main__':
    s = 'cbaebabacd'
    p = 'abc'
    S = Solution()
    print(S.findAnagrams(s,p))
