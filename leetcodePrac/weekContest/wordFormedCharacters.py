#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/8/18 10:34
# @Author   : Daishijun
# @Site     : 
# @File     :
# @Software : PyCharm

'''5048 拼写单词'''


class Solution:
    def countCharacters(self, words, chars: str) -> int:
        charmap = {}
        for s in chars:
            charmap[s] = charmap.get(s, 0) +1
        res = 0
        backup = charmap.copy()
        for word in words:

            charmap = backup.copy()
            res += len(word)
            for ss in word:
                charmap[ss] = charmap.get(ss, 0)-1
                if charmap[ss] <0:
                    print('invalid:', word)
                    print('map:', charmap)
                    res -=len(word)
                    break

        return res

if __name__ == '__main__':
    words = ["hello","world","leetcode"]
    chars = "welldonehoneyr"
    S = Solution()
    print(S.countCharacters(words, chars))

