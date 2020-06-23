#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/6/23 21:08 
# @Author : magician 
# @File : 88.py 
# @Software: PyCharm


# 88. 合并两个有序数组
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#  
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]


# 思路：运用双指针，比较两个有序list，找到最小值，然后不断的将较小值插入新的数列

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #若强制要求num1被替换，则将num1复制后，再将num1置空，然后操作复制list
        n1,n2=0,0
        tmp_lis=[]
        # mind=0

        while n1<m and n2<n:
            if nums1[n1]<nums2[n2]:
                tmp_lis.append(nums1[n1])
                n1+=1
            else:
                tmp_lis.append(nums2[n2])
                n2+=1
        print(tmp_lis)
        tmp_lis+=nums1[n1:m]
        tmp_lis+=nums2[n2:n]
        print(tmp_lis)
        #注意这样写结果有误
        # nums1=tmp_lis
        nums1[:]=tmp_lis[:]
        return nums1




