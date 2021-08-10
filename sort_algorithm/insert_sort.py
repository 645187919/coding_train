#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-10 21:15 
# @Author : magician 
# @File : insert_sirt.py 
# @Software: PyCharm



alist = [54,26,93,17,77,31,44,55,20]


def insert_sort(alist):
    #再写外层循环,需要确定n-1个元素后整个队列才有序。
    for i in range(len(alist)-1):
        j=i
        #先写内层循环用于拿右边无序序列中的一个元素和左边的有序序列中的元素两两比较，插入到合适的位置。
        #j为左边排序数组的最后一个元素
        while j>=0:
            #查看排序数组的最大元素和未排序的元素的大小关系，若小于，则直接break，换下一个未排序元素，否则依次比较。
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                j-=1
            else:
                break

print(alist)
insert_sort(alist)
print(alist)
