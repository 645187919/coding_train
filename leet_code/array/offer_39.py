#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-11-02 20:51 
# @Author : magician 
# @File : offer_39.py 
# @Software: PyCharm



# 剑指 Offer 39. 数组中出现次数超过一半的数字
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 示例 1:
#
# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2
# 限制：
# 1 <= 数组长度 <= 50000


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        len_nums=len(nums)//2
        for i in nums:
            dic[i]=dic.get(i,0)+1
            if dic[i]>len_nums:
                return i
