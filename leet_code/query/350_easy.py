#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-26 20:31 
# @Author : magician 
# @File : 350_easy.py 
# @Software: PyCharm

# 350. 两个数组的交集 II
# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1：
#
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 示例 2:
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
#
#
# 说明：
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。

#思路：用map来存储数据，key为元素，val为频次，然后遍历另一个数组，对于重复的元素，则对val做减法。

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #map用于记录某个数组出现的频次，根据频次再把交集进行追加
        tmp_dic={}
        tmp_list=[]

        for i in nums1:
            if tmp_dic.get(i) is None:
                tmp_dic[i]=1
            else:
                tmp_dic[i]+=1
        print(tmp_dic)

        for j in nums2:
            if tmp_dic.get(j) is not None and tmp_dic[j]!=0:
                tmp_list.append(j)
                tmp_dic[j]-=1

        return tmp_list




