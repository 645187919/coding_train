#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-26 20:18 
# @Author : magician 
# @File : 349.py 
# @Software: PyCharm

# 349. 两个数组的交集
# 给定两个数组，编写一个函数来计算它们的交集。
#
#
#
# 示例 1：
#
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2]
# 示例 2：
#
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[9,4]
#

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #方法一：暴力解法，依次遍历两个数组比较大小。O(n2)
        # num1_set=set(nums1)
        # num2_set=set(nums2)

        # tmp_lis=[]


        # for i in num1_set:
        #     for j in num2_set:
        #         if i==j:
        #             tmp_lis.append(i)
        #         else:
        #             continue
        # return tmp_lis

        #方法二：将其中一个数组转化为map，遍历另一个数组，查看是否在map中

        num2_set=set(nums2)

        tmp_lis=[]
        tmp_dic={}
        for i in nums1:
            tmp_dic[i]=1
        for j in num2_set:
            #get()方法若没找到key默认返回None
            if tmp_dic.get(j) is not None:
                tmp_lis.append(j)
        return tmp_lis








