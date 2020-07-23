#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/23 21:43 
# @Author : magician 
# @File : quick_sort_3_way.py 
# @Software: PyCharm


def quick_sort(alist,l,r):
    #声明基准元素
    base=alist[l]
    i=l+1
    lt=l+1
    #便于后续大于base区域的操作。先扩充区域然后填充元素。若gt=r，则后续操作变成先填充元素，再扩充区域，多出来一个空位�?
    gt=r+1
    print(lt,i,gt)
    #终止条件
    while i<gt:#gt为length，所以为小于
        if alist[i]<base:
            #lt已经有位置所以可以先交换位置，再+1
            alist[i],alist[lt]=alist[lt],alist[i]
            i+=1
            lt+=1
        elif alist[i]>base:
            #gt先扩充位位置
            gt-=1
            #由于互换位置后，元素并未被遍历，所以i不能+1
            alist[i],alist[gt]=alist[gt],alist[i]
        else:
            i+=1
    #lt多一个位置，所以需要回到末尾的索引处和base元素交换
    alist[l],alist[lt-1]=alist[lt-1],alist[l]
    #返回等于base区域的前后索引
    return lt-1,gt



def quick_sort_3_way(alist,l,r):
    #终止条件
    if l>=r:
        return

    mind1,mind2 = quick_sort(alist, l,r)
    quick_sort_3_way(alist,l,mind1)
    quick_sort_3_way(alist,mind2,r)
    return alist

import time
strat = time.time()
a=[2,2,3,1,2,6,1,6,3,2,6,5,4,3,2,1,4,5,3,5,3,2,1,2,3,2,1]
print(a)
print(quick_sort_3_way(a,0,len(a)-1))
print(time.time() - strat)