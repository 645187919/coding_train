#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/20 21:45 
# @Author : magician 
# @File : __init__.py.py 
# @Software: PyCharm


def quick_sort(alist,start,end):

    if start>end:
        return
    #基准元素
    mind=alist[start]
    low=start
    high=end
    while low<high:
        while low<high and mind<=alist[high]:
            high-=1
        alist[high],alist[low]=alist[low],alist[high]

        while low<high and mind>=alist[low]:
            low+=1
        alist[high],alist[low]=alist[low],alist[high]

    alist[low]=mind
    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)

alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)