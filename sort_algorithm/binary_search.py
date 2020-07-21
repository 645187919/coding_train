#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/21 20:05 
# @Author : magician 
# @File : binary_search.py 
# @Software: PyCharm


def binary_search(alist,target):

    n=len(alist)
    l,r=0,n-1#l,r分别代表要在索引为[l,r]范围内查找target

    while l<=r:#l=r时，[l,r]仍为一个数组范围，所以可以等于
        mind=(l+r)//2
        if alist[mind]==target:
            return True
        elif alist[mind]>target:
            r=mind-1   #target在 [l,mind-1]之间
        else:
            l=mind+1   #target在[mind+1,r]之间
    return False


li=[17, 20, 26, 31, 44, 54, 55, 77, 93]

print(binary_search(li, 20))
print(binary_search(li, 2))


