# -*- coding: utf-8 -*-
# @Date    : 2019/5/7
# @Time    : 19:31
# @Author  : Daishijun
# @File    : pathArrayToStatisticArray.py
# Software : PyCharm

'''
路径数组变为统计数组
'''
'''
初始给的paths[]给定的是第i号城市与下一个城市连通，其实是无向图。先转换成第i号城市距离首都的距离，在paths[]上原地修改，然后根据距离[]改出统计数组，原地
'''

def pathsToDistance(paths):
    cap = 0 #用于标记首都的位置
    for i in range(len(paths)):
        if paths[i] == i:
            cap = i
        elif paths[i] >-1:    #没有遍历过且不是首都
            curI = paths[i]
            paths[i] = -1    #作为起点
            preI = i    #回跳标记
            while paths[curI] != curI:    #每到首都
                if paths[curI] >-1:
                    nextI = paths[curI]
                    paths[curI] = preI     #记录回跳地点
                    preI = curI
                    curI = nextI
                else:    #计算过距离了
                    break
            #找到首都之后，curI == nextI == 首都标号
            value = 0 if paths[curI] == curI else paths[curI]    #如果是遍历到了首都，说明中间的路径上都是第一次计算的，所以此时记录首都到首都的距离为0； 不然的话，记录下中转点到首都的距离，后续回跳的时候要-1
            #此时preI记录的是上一个回跳点
            while paths[preI] != -1:
                lastPreI = paths[preI]    #记录下回跳点，后面要把Paths[i]位置的表示意义改成距离首都距离了。
                paths[preI] = value -1
                value -=1
                curI = preI
                preI = lastPreI
            paths[preI] = value-1
            value -=1
    paths[cap] = 0

def distanceToNums(disArr):
    for i in range(len(disArr)):
        index = disArr[i]
        if index <0:    #表示该点仍然表示城市距离首都的距离
            disArr[i] =0
            while 1:
                index = -index    #距离
                if disArr[index] >-1:    #已经在表示距离首都index远的城市个数
                    disArr[index] +=1
                    break
                else:
                    nextIndex = disArr[index]    #记录当前index城市距离首都距离
                    disArr[index] = 1
                    index = nextIndex
    disArr[0] = 1    #距离首都距离为0 的只有1个首都，题目给定的



if __name__ =='__main__':
    paths = [9,1,4,9,0,4,8,9,0,1]
    pathsToDistance(paths)
    print(paths)
    distanceToNums(paths)
    print(paths)
