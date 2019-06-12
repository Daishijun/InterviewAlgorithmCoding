# -*- coding: utf-8 -*-
# @Date    : 2019/6/9
# @Time    : 23:42
# @Author  : Daishijun
# @File    : letterDiffPosGroup.py
# Software : PyCharm

'''Leetcode 49 字母异位词分组'''


class Solution:
    def groupAnagrams(self, strs):
        letters = [0 for i in range(26)]
        dic = {}
        for s in strs:
            lett = letters[:]
            for letter in s:
                lett[ord(letter)- 97] +=1
            tup = tuple(lett)
            if tup in dic.keys():
                dic[tup].append(s)
            else:
                dic[tup] = [s]
        return [v for k,v in dic.items()]

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    S = Solution()
    print(S.groupAnagrams(strs))