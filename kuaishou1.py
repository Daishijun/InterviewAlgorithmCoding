# -*- coding: utf-8 -*-
# @Date    : 2019/4/13
# @Time    : 16:19
# @Author  : Daishijun
# @File    : kuaishou1.py
# Software : PyCharm

def find(s1, s2):
    m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]
    mmax=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1]=m[i][j]+1
                if m[i+1][j+1]>mmax:
                    mmax=m[i+1][j+1]
    return mmax

def find_lcsubstr(s1, s2):  #输出长公共子串,长度.
    m=[[0 for i in range(len(s2)+1)]  for j in range(len(s1)+1)]  #生成0矩阵，为方便后续计算，比字符串长度多了一列
    mmax=0   #最长匹配的长度
    p=0  #最长匹配对应在s1中的最后一位
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                m[i+1][j+1]=m[i][j]+1
                if m[i+1][j+1]>mmax:
                    mmax=m[i+1][j+1]
                    p=i+1
    return s1[p-mmax:p],mmax   #返回最长子串及其长度




if __name__ == '__main__':
    str1, str2 = input().split(',')
    print(find(str1,str2))