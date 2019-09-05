# -*- coding: utf-8 -*-
# @Date    : 2019/6/3
# @Time    : 14:17
# @Author  : Daishijun
# @File    : huiwenString.py
# Software : PyCharm

'''Leetcode 647 回文子串'''

'''
在manacher的基础上，根据每次的回文半径，计算第i位置为中心的回文子串个数，做累加。
'''
class Solution:
    def countSubstrings(self, s) -> int:

        def insertManacherStr(s):
            res = ['#']
            for i in range(len(s)):
                res.append(s[i])
                res.append('#')
            return res
        sinsertlist = insertManacherStr(s)
        pArr = [0 for i in range(len(sinsertlist))]
        index = 0
        pR = 0
        count = 0
        for i in range(len(sinsertlist)):
            if pR > 1:
                pArr[i] = min(pR-i, pArr[index-(i-index)])
            else:
                pArr[i] = 1
            while i+pArr[i] < len(sinsertlist) and i-pArr[i] > -1:
                if sinsertlist[i+pArr[i]] == sinsertlist[i-pArr[i]]:
                    pArr[i] +=1
                else:
                    break
            if i+pArr[i] > pR:
                index = i
                pR = i+pArr[i]
            count += pArr[i]>>1
        return count

'''leetcode 5 最长回文子串, 返回子串
Manacher 做法
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s):
            res = [0 for i in range(2*len(s)+1)]
            sind = 0
            for i in range(len(res)):
                if not i&1:
                    res[i] = '#'
                else:
                    res[i] = s[sind]
                    sind +=1
            return res
        slist = manacher(s)
        pArr = [0 for i in range(len(slist))]
        pR = 0
        index = 0
        maxlen = 0
        maxind = 0
        for i in range(len(slist)):
            pArr[i] = 1 if pR<=i else min(pR-i, pArr[2*index-i])
            while i+pArr[i] < len(slist) and i-pArr[i] >-1:
                if slist[i+pArr[i]] == slist[i-pArr[i]]:
                    pArr[i] +=1
                else:
                    break
            if i+pArr[i] > pR :
                pR = i+ pArr[i]
                index = i
            if maxlen < pArr[i]:
                maxind = i
                maxlen = pArr[i]
            if pR == len(slist):
                break
        print('maxlength:', maxlen, '\tmaxind:', maxind)
        substrlist = slist[maxind-maxlen+1: maxind+maxlen]
        print('sublist:', substrlist)

        substr = ''.join(substrlist)

        return substr.replace('#','')


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_len = 1
        n = len(s)
        start = 0
        for i in range(1, n):
            even = s[i - max_len:i + 1]    #偶数    #并不是以i位置字符为中心，而是以i位置为结尾
            print('iter:', i, '\teven:', even)
            odd = s[i - max_len - 1:i + 1]    #奇数
            print('iter:', i, '\todd:', odd, 'i-maxlen-1:', i - max_len - 1)
            # print(even,odd)
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
            elif i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1

        # print(start,max_len)
        return s[start: start + max_len]

if __name__ == '__main__':
    # string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    string = 'babad'
    S = Solution()
    print(S.longestPalindrome(string))

    print(string[-1:2])