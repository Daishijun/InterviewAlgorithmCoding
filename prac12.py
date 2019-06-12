# -*- coding: utf-8 -*-
# @Date    : 2019/6/1
# @Time    : 20:44
# @Author  : Daishijun
# @File    : prac12.py
# Software : PyCharm
#
string = input()
strlist = input().split()

def splits(strlist, resstr):
    if resstr == '':
        return True
    for s in strlist:
        if s not in resstr:
            continue
        if resstr.index(s) == 0:
            resstr = resstr.split(s,1)

            if len(resstr)==2:
                resstr = resstr[1]

                flag = splits(strlist, resstr)
                if flag:
                    return flag
    return False
#
print(splits(strlist,string))
#
# def test1(strlist, resstr):
#     flag = True
#     for s in strlist:
#         flag = flag and (s in resstr)
#     return flag

# if __name__ == "__main__":
#     s = 'asdasdv'
#     print(s.index('as'))