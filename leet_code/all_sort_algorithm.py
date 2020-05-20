#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/5/20 14:57 
# @Author : magician 
# @File : all_sort_algorithm.py 
# @Software: PyCharm


# #1、冒泡排序
# def bubble_sort(alist):
#
#     n = len(alist)
#     #外层循环要执行n-1次
#     for i in range(n-1):
#         # 内部要两两比较将大值放到最后一位
#         for j in range(n-i-1):
#             if alist[j]>alist[j+1]:
#                 alist[j],alist[j+1]=alist[j+1],alist[j]
#
#
#     return alist
#
##时间复杂度O（n）或者O（n2）
# def bubble_sort_better(alist):
#
#     n = len(alist)
#     count=0
#     #外层循环要执行n-1次(每次将一位最大值放到最后一位)
#     for i in range(n-1):
#         # 内部要两两比较将大值放到最后一位
#         for j in range(n-i-1):
#             if alist[j]>alist[j+1]:
#                 alist[j],alist[j+1]=alist[j+1],alist[j]
#                 count+=1
#         if count==0:
#             return alist
#
#
#     return alist
# li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(li)
# bubble_sort_better(li)
# print(li)


# 2、选择排序
#原理：它的工作原理如下。首先在未排序序列中找到最小（大）元素，
# 存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾

#思路：首先需要一个min坐标标记最小值，之后对右边的无序序列进行遍历选择操作，若找到比min值还小的数就交换位置
# <与冒泡的区别：冒泡两两比较将大的值往后移，选择是设定一个min的索引然后拿选定的最小值和右边的无序序列分别进行遍历比较，
# 最终得到最小值与min索引指向的值进行交换。
def select_sort(alist):

    n = len(alist)
    #外层循环用于控制寻找最大元素的次数
    for i in range(n):
        min_index=i
        #内层循环用于交换最大元素与末尾元素
        for j in range(i+1,n):
            if alist[min_index]>alist[j]:
                min_index=j

        alist[i],alist[min_index]=alist[min_index],alist[i]
    return alist

li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(li)
select_sort(li)
print(li)

#3、插入排序
#原理：它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，
# 在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
# 思路：从右边的无序序列中拿数据插入到左边的有序序列中。

# def insert_sort(alist):
#     n=len(alist)
#     #外层循环控已经排好序的元素所需的次数。
#     for i in range(n):
#         #j代表已经排好序的元数数
#         j=i
#         #拆入数据需要比较的元素的限制条件
#         while j>0:
#             if alist[j]>alist[j+1]:
#                 alist[]



# 2、快速排序
#通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
#
def quick_sort(alist,start,end):
    mind=(end-start)/2

