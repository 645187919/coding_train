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


# 思路：合并两个有序数组：
# 运用双指针，比较两个有序list，找到最小值，然后不断的将较小值插入新的数列。直到某个list的值被插完。
#接下来，将另一个list的剩余值插入新的数列即可

#参考：https://leetcode-cn.com/problems/merge-sorted-array/solution/gelthin-gui-bing-pai-xu-by-gelthin/
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #若强制要求num1被替换，则将num1复制后，再将num1置空，然后操作复制list
        n1,n2=0,0
        num1_copy=nums1[:m]
        nums1[:]=[]

        # mind=0

        while n1<m and n2<n:
            if num1_copy[n1]<nums2[n2]:
                nums1.append(num1_copy[n1])
                n1+=1
            else:
                nums1.append(nums2[n2])
                n2+=1
        print(nums1)
        nums1+=num1_copy[n1:m]
        nums1+=nums2[n2:n]
        print(nums1)
        #注意这样写结果有误
        # num1=A：num1指向A的存储地址；num1[:]=A[:]：代表将A的值赋值给num1
        # nums1=nums1
        # nums1[:]=nums1[:]
        return nums1



    #第二次写
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_i=0
        n_i=0
        tmp=[]
        while m_i<m and n_i<n:
            if nums1[m_i]>nums2[n_i]:
                tmp.append(nums2[n_i])
                n_i+=1
            else:
                tmp.append(nums1[m_i])
                m_i+=1

        tmp=tmp+nums1[m_i:m]
        tmp=tmp+nums2[n_i:n]
        return nums1
