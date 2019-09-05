#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/7/29 22:10
# @Author   : Daishijun
# @Site     : 
# @File     : keyboardPath.py
# @Software : PyCharm

'''Leetcode 1138 字母板上的路径'''
'''
从别的字符到z需要特殊考虑，因为不能直接D下来。
'''

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        letterMap = {'a':[0,0],'b':[0,1],'c':[0,2],'d':[0,3],'e':[0,4],\
                     'f':[1,0],'g':[1,1],'h':[1,2],'i':[1,3],'j':[1,4],\
                     'k':[2,0],'l':[2,1],'m':[2,2],'n':[2,3],'o':[2,4],\
                     'p':[3,0],'q':[3,1],'r':[3,2],'s':[3,3],'t':[3,4],\
                     'u':[4,0],'v':[4,1],'w':[4,2],'x':[4,3],'y':[4,4],\
                     'z':[5,0]}
        frompos = [0,0]
        res = ''
        for letter in target:
            topos = letterMap[letter]
            # print('topos:',topos, 'from:',frompos)
            # print('start, res:',res)
            if topos == frompos:
                res = res + '!'

            else:
                rowdiff = topos[0]-frompos[0]
                coldiff = topos[1]-frompos[1]
                if letter == 'z':
                    for i in range(abs(rowdiff)-1):
                        res = res + ('D' if rowdiff > 0 else 'U')
                    for j in range(abs(coldiff)):
                        res = res + ('R' if coldiff > 0 else 'L')
                    res = res + ('D' if rowdiff > 0 else 'U')
                else:
                    for i in range(abs(rowdiff)):

                        res = res + ('D' if rowdiff>0 else 'U')

                    for j in range(abs(coldiff)):
                        res = res + ('R' if coldiff>0 else 'L')
                res = res + '!'
            frompos = topos
            # print('topos:',topos, 'res:',res, 'frompos:',frompos)
        return res

if __name__ == '__main__':
    target = 'zdz'
    S = Solution()
    print(S.alphabetBoardPath(target))