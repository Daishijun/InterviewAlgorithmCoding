# -*- coding: utf-8 -*-
# @Date    : 2019/5/26
# @Time    : 15:20
# @Author  : Daishijun
# @File    : prac.py
# Software : PyCharm

# string = 'abcabc'
# def prefix(string):
#     res = [0 for i in range(len(string)+1)]
#     charset = set(list(string))
#     res[0] = {x:0 for x in charset}
#     for i in range(len(string)):
#         res[i+1] = res[i].copy()
#         res[i+1][string[i]] = res[i][string[i]]+1
#     return res
# print(prefix(string))

def inter(p1, p2):
    left = max(p1[0],p2[0])
    right = min(p1[1], p2[1])
    if left<=right:
        return [left, right]
    else:
        return p2

if __name__ == '__main__':
    p1 = [0,2]
    p2 = [3,4]
    print(inter(p1, p2))