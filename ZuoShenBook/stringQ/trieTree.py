# -*- coding: utf-8 -*-
# @Date    : 2019/4/25
# @Time    : 20:20
# @Author  : Daishijun
# @File    : trieTree.py
# Software : PyCharm

'''
构建一个trie数，实现插入，删除，查找，以pre为前缀的单词数量这4种功能。
'''

class TrieNode():
    def __init__(self):
        self.path = 0     #记录有多少个单词共用当前节点====》因为要提供查询以pre 为前缀的单词数量这一个功能
        self.end = 0    #表示有多少个单词以这个节点作为结尾
        #  ===》能够知道已经建好的trie树中有多少个相同的该字符串。
        # ===》支持查询功能，因为要查找的string可能是之前加入字典数的一个前缀，所以需要标记每个节点位置是否仅仅是中间节点。
        self.map = [None for i in range(26)]    #26个字母

class TrieTree():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return
        node = self.root
        node.path +=1
        for s in word:
            index = ord(s) - ord('a')
            if node.map[index] == None:
                node.map[index] = TrieNode()    #插入节点
            node = node.map[index]
            node.path +=1
        node.end +=1

    def search(self, word):
        if not word:
            return False
        node = self.root
        for s in word:
            index = ord(s) - ord('a')
            if node.map[index] == None:
                return False
            node = node.map[index]
        return node.end != 0

    def delete(self, word):
        if self.search(word):
            node = self.root
            node.path -=1
            for s in word:
                index = ord(s) - ord('a')
                if node.map[index].path == 1:
                    node.map[index] = None
                    return
                node.map[index].path -=1
                node = node.map[index]
            node.end -=1

    def prefixNum(self, pre):
        if not pre:
            return 0
        node = self.root
        for s in pre:
            index = ord(s) - ord('a')
            if node.map[index] == None:
                return 0
            node = node.map[index]
        return node.path

if __name__ == '__main__':
    trie = TrieTree()
    trie.insert('abc')
    trie.insert('abcd')
    trie.insert('abd')
    trie.insert('b')
    print(trie.search('abc'))
    print(trie.search('abe'))
    print(trie.prefixNum('ab'))

