# -*- coding: utf-8 -*-
# @Date    : 2019/5/18
# @Time    : 11:41
# @Author  : Daishijun
# @File    : PreAndInoderToPos.py
# Software : PyCharm

'''
通过先序和中序数组生成后序数组
'''

def setPos(pre, pi, pj, inoder, ini, inj, pos, posi, mapdict):
    if pi>pj:
        return posi
    pos[posi] = pre[pi]
    posi -=1
    rootindex = mapdict[pre[pi]]

    posi = setPos(pre, pj-(inj-rootindex)+1 ,pj, inoder, rootindex+1,inj, pos, posi, mapdict)
    posi = setPos(pre, pi+1, pi+1+(rootindex-ini)-1, inoder, ini, rootindex-1, pos, posi, mapdict)    #从中序数组中找到当前节点的左右子树序列长度，根据这个长度在先序数组上划分边界很重要。
    # print('posi:', posi)
    return posi

def getPosArray(pre, inorder):
    #要根据pre中的值，迅速找到inorder中相应值所在的位置，从而划分出左右子序列。
    if not pre or not inorder:
        return None
    length = len(pre)
    pos = [0 for i in range(length)]
    mapdict = {}
    for i in range(length):
        mapdict[inorder[i]] = i    #需要记录中序中元素对应的位置，用以计算左右序列长度
    setPos(pre,0, length-1, inorder, 0, length-1, pos, length-1, mapdict)
    return pos

if __name__ == '__main__':
    pre = [1,2,4,5,3,6,7]
    inorder = [4,2,5,1,6,3,7]
    print(getPosArray(pre, inorder))