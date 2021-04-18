#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-04-18 16:26 
# @Author : magician 
# @File : 35_easy.py 
# @Software: PyCharm


# 35. 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0

#思路：注意是一个有序的数组，且没有重复元素。所以可以考虑用二分查找法；
#其次，注意对应的几种情况：当target在数组中间（等于数组元素与在数组元素之间），在数组左边，在数组右边
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # #方法一暴力解法：
        # length=len(nums)
        # for i in range(length):
        #     #target在数组左边
        #     #target在数据中间
        #     if nums[i]>=target:
        #         return i
        # #target在数组右边
        # return length




        #方法二：二分查找法
        left=0
        right=len(nums)-1 #不动循环变量【0~length-1】

        #target在数据中间，在数据左边，在数组右边

        #在左边
        if target<nums[0]:
            return 0
        #在中间
        while left<=right:
            mind=(right+left)//2
            if nums[mind]>target:
                right=mind-1
            elif nums[mind]<target:
                left=mind+1
            else:
                return mind
        #在右边
        return right+1



