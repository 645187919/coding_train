#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/20 21:45 
# @Author : magician 
# @File : quick_sort.py 
# @Software: PyCharm



def quick_sort(alist,start,end):

    #递归实现
    #首先终止条件：指针交汇时终止
    if start>end:
        return
    #双指针
    low=start
    high=end
    #声明基准元素，又腾出来一个位置，便于其他元素移位。
    mind=alist[low]

    while low<high:
        #从右往左将数组元素和基准元素进行对比，若小于基准元素则移到下一位，否则则交换元素位置（刚好有一个空缺的基准元素的位置）
        while low<high and mind<=alist[high]:
            high-=1
        alist[high],alist[low]=alist[low],alist[high]

        while low<high and mind>=alist[low]:
            low+=1
        alist[high],alist[low]=alist[low],alist[high]
    #将比较元素插入已经确定位置的地方（一个元素的位置已确定！）
    alist[low]=mind
    #分别确定基准元素两边的数据元素。
    quick_sort(alist,start,low-1)
    quick_sort(alist,low+1,end)

if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)



