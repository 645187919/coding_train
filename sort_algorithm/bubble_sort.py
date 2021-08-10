#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-03 21:09 
# @Author : magician 
# @File : bubble_sort.py 
# @Software: PyCharm


def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            #比较两个数的大小，大的往后延。
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
            else:
                continue


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    bubble_sort(li)
    print(li)

