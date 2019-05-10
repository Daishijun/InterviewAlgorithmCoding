# -*- coding: utf-8 -*-
# @Date    : 2019/4/23
# @Time    : 16:35
# @Author  : Daishijun
# @File    : stringChangePath.py
# Software : PyCharm
'''
字符串的路径转换
'''

def getNext(word, wordset):
    wlist = list(word)
    res = []
    for chari in range(ord('a'), ord('z')+1):
        char = chr(chari)
        for i in range(len(wlist)):
            if wlist[i] != char:
                tmp = wlist[i]
                wlist[i] = char
                if ''.join(wlist) in wordset:
                    res.append(''.join(wlist))
                wlist[i] = tmp
    return res

def getNexts(words):
    '''
    从包含所有word的list中生成Next信息，即只更改一个字符所能变成的set中的字符串。words中没有有重复的字符串。
    :param words:
    :return:
    '''
    # wordset = set(words)
    nexts = {}
    for word in words:
        nexts[word] = getNext(word, words)
    return nexts

def getDistances(start, nexts):
    distances = {}
    distances[start] = 0
    queue = [start]
    hset = set()
    hset.add(start)
    while queue:
        cur = queue.pop(0)
        for stri in nexts[cur]:
            if stri not in hset:
                distances[stri] = distances.get(cur)+1
                queue.append(stri)
                hset.add(stri)
    return distances

def getShortestPaths(cur, to, nexts, distances, solution, res):
    '''

    :param cur: 当前节点
    :param to: 目标节点
    :param nexts:  nexts字典信息
    :param distances: distances字典信息
    :param solution: 路径list
    :param res:  不同的路径组成的list
    :return: None
    '''
    solution.append(cur)
    if to == cur:
        res.append(solution.copy())
    else:
        for next in nexts.get(cur):
            if distances.get(next) == distances.get(cur)+1:    #这个distances距离字典都是从start开始到各个节点的距离。
                getShortestPaths(next, to, nexts, distances, solution, res)

    solution.pop()


if __name__ == '__main__':
    # word = 'aa'
    # wordlist = ['ac','ab','ba','bd']
    # print(getNext(word, wordlist))

    start = 'abc'; end = 'cab'; wordlist = ['cab', 'acc', 'cbc', 'ccc', 'cac', 'cbb', 'aab', 'abb']

    wordlist.append(start)
    nexts = getNexts(wordlist)
    for key, val in nexts.items():
        print(key, val)

    dis = getDistances(start, nexts)
    for k, v in dis.items():
        print(k, v)

    path = []
    res= []
    getShortestPaths(cur=start, to=end, nexts=nexts, distances=dis, solution=path, res=res)
    print(res)
    print(len(res))