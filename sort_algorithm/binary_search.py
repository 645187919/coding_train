#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/21 20:05 
# @Author : magician 
# @File : binary_search.py 
# @Software: PyCharm


def binary_search(alist,target):

    n=len(alist)
    l,r=0,n-1#l,r分别代表要在索引为[l,r]范围内查找target（循环不变量）

    while l<=r:#l=r时，[l,r]仍为有效区间，所以可以等于
        # mind=(l+r)//2  #加法，当两个数都比较大的时候可能会差生整型溢出的风险，所以改为下面的形式
        mind=(l+(r-1))//2
        if alist[mind]==target:
            return mind
        elif alist[mind]>target:
            r=mind-1   #target在 [l,mind-1]之间
        else:
            l=mind+1   #target在[mind+1,r]之间
    return -1

def binary_search_2(alist,target):
    n=len(alist)
    l,r=0,n  #l,r分别代表要在索引为[l,r)范围内查找target（循环不变量）
    while l<r:
        mind=(l+(r-l))//2
        if alist[mind]==target:
            return mind
        elif alist[mind]>target:
            r=mind   #[l,r).右边维闭区间。
        else:
            l=mind+1
    return -1




li=[17, 20, 26, 31, 44, 54, 55, 77, 93]

print(binary_search(li, 20))
print(binary_search(li, 2))


print(binary_search_2(li, 20))
print(binary_search_2(li, 2))