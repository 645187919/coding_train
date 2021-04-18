#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-04-18 15:23 
# @Author : magician 
# @File : demo.py 
# @Software: PyCharm


def two_search(lis,target):
    n=len(lis)
    star=0
    end=n-1
    while star<=end:
        mid=(star+(end-star))//2
        print(mid)
        if lis[mid]==target:
            return mid
        elif lis[mid]<target:
            star=mid+1
        else:
            end=mid-1
    return -1

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

def binary_search(lis, num):
    left = 0
    right = len(lis) - 1
    while left <= right:   #循环条件
        mid = (left + right) // 2   #获取中间位置，数字的索引（序列前提是有序的）
        if num < lis[mid]:  #如果查询数字比中间数字小，那就去二分后的左边找，
            right = mid - 1   #来到左边后，需要将右变的边界换为mid-1
        elif num > lis[mid]:   #如果查询数字比中间数字大，那么去二分后的右边找
            left = mid + 1    #来到右边后，需要将左边的边界换为mid+1
        else:
            return mid  #如果查询数字刚好为中间值，返回该值得索引
    return -1  #如果循环结束，左边大于了右边，代表没有找到


li=[17, 20, 26, 31, 44, 54, 55, 77, 93]

print(binary_search(li, 21))

