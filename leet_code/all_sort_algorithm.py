#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/5/20 14:57 
# @Author : magician 
# @File : all_sort_algorithm.py 
# @Software: PyCharm


# #1、冒泡排序
# def bubble_sort(alist):
#     n = len(alist)
#
#     if alist is None or n<2:
#         return
#
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
# #时间复杂度O（n）或者O（n2）
# def bubble_sort_better(alist):
#
#     n = len(alist)
#     if alist is None or n<2:
#         print("not need sort")
#         return
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
# def select_sort(alist):
#
#
#     count=0
#     n = len(alist)
#     if alist is None or n<2:
#         print("not need sort")
#         return
#
#     #确定n-1个最小值（n-1次循环）
#     for i in range(n-1):
#         min_index=i
#         #两两比较，将最小值放在初始位置，先用索引记录，最终再交换。
#         for j in range(i+1,n):
#             if alist[min_index]>alist[j]:
#                 min_index=j
#         if count==0:
#             return alist
#         alist[i],alist[min_index]=alist[min_index],alist[i]
#     return alist
#
# li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(li)
# select_sort(li)
# print(li)

#3、插入排序
#原理：它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，
# 在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
# 思路：从右边的无序序列中拿数据插入到左边的有序序列中。
#
# #像打扑克排一样，每次抓牌将无序的牌插入到有序的牌中。
# def insert_sort(alist):
#     n=len(alist)
#     if alist is None or n<2:
#         return
#     #外层循环控需要插入左边已经排好序队列中的元素（n个元素需要n-1次排序，）
#     for i in range(1,n):
#         #j代表已经排好序的元数数
#         j=i-1
#         #拆入数据需要比较的元素的限制条件
#         # for j in range(i-1)[::-1]:
#         while j>=0:
#             if alist[j]>alist[j+1]:
#                 alist[j],alist[j+1]=alist[j+1],alist[j]
#             j-=1
#
# li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(li)
# insert_sort(li)
# print(li)

# 2、快速排序
#通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
# #
# def quick_sort(alist,start,end):
#     mind=(end-start)/2


#归并排序
#
# def merge_sort(alist):
#     n=len(alist)
#     if n<=1:
#         return alist
#     mid=n//2
#     left_ali = merge_sort(alist[:mid])
#     right_ali=merge_sort(alist[mid:])
#
#     left_point,right_point=0,0
#     result=[]
#     while left_point<len(left_ali) and right_point<len(right_ali):
#         if left_ali[left_point]<=right_ali[right_point]:
#             result.append(left_ali[left_point])
#             left_point+=1
#         else:
#             result.append(right_ali[right_point])
#             right_point+=1
#
#     result+=left_ali[left_point:]
#     result+=right_ali[right_point:]
#     return result
#
#
# li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(li)
# sorted_li = merge_sort(li)
# print(sorted_li)

def merge_sort(alist):
    n=len(alist)
    if alist is None or n<2:
        return alist

    #先将数组分成两列分别排序
    mid=n//2
    ali_lef=merge_sort(alist[:mid])
    ali_right=merge_sort(alist[mid:])
    #再将两列已排序数组进行排序
    result=[]

    left_pi,right_pi=0,0
    while left_pi<len(ali_lef) and right_pi<len(ali_right):
        if ali_lef[left_pi]<ali_right[right_pi]:
            result.append(ali_lef[left_pi])
            left_pi+=1
        else:
            result.append(ali_right[right_pi])
            right_pi+=1

    result+=ali_lef[left_pi:]
    result+=ali_right[right_pi:]

    return result

li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(li)
sorted_li = merge_sort(li)
print(sorted_li)



#二分查找

def two_find(alist,target):
    #
    n=len(alist)
    l,r=0,n-1
    if target is None:
        return -1
    # mid=//2
    #非递归的方法，限制条件l<r
    while l<r:
        mid=(l+r)//2
        if target==alist[mid]:
            return mid
        elif target>alist[mid]:
            l=mid+1
        else:
            r=mid-1
    return False

li=[17, 20, 26, 31, 44, 54, 55, 77, 93]
# print(two_find(li,31))

# print(li[2:3])





