# -*- coding: utf-8 -*-
# @Date    : 2019/4/25
# @Time    : 10:07
# @Author  : Daishijun
# @File    : minSubstringLength.py
# Software : PyCharm
'''
最小包含子串的长度
string1的子串中包含string2全部字符的最短子串长度
'''

'''
双指针， map记录待匹配字符
'''


def minLength(string1, string2):
    mapdict = [0 for i in range(256)]
    left = 0
    right = 0
    waitmatch = len(string2)
    minlen = float('inf')
    for s2 in string2:
        mapdict[ord(s2)] +=1
    while right <len(string1):
        mapdict[ord(string1[right])] -=1
        if mapdict[ord(string1[right])]>=0:
            waitmatch -=1
        if waitmatch == 0:
            while mapdict[ord(string1[left])]<0:
                mapdict[ord(string1[left])] +=1
                left +=1

            # print('left:{l}, right:{r}'.format(l=left, r=right))
            minlen = min(right- left+1, minlen)
            mapdict[ord(string1[left])] +=1
            left +=1
            waitmatch +=1
        right +=1
    if minlen == float('inf'):
        return 0
    else:
        return minlen

if __name__ == '__main__':
    string1 = 'adabbca'

    string2 = 'acb'

    print(minLength(string1, string2))