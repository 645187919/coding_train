#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/21 21:14 
# @Author : magician 
# @File : __init__.py.py 
# @Software: PyCharm


def quick_sort(alist,start,end):

    if start>end:
        return
    #先写内层循环
    low=start
    high=end
    #low作为基准元素
    mind=alist[low]

    while low<high:
        if  mind>=alist[high]:
            alist[high],alist[low]=alist[low],alist[high]
            low+=1
        else:
            high-=1
        if low<high and mind<=alist[low]:
            alist[high],alist[low]=alist[low],alist[high]
            high-=1
        else:
            low+=1

    alist[low]=mind
    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)

if __name__ == "__main__":
    alist = [54,26,93,17,77,31,44,55,20]
    print(alist)
    quick_sort(alist,0,len(alist)-1)
    print(alist)