#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-02 17:37 
# @Author : magician 
# @File : 219_easy.py 
# @Software: PyCharm



# 219. 存在重复元素 II
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，
# 并且 i 和 j 的差的 绝对值 至多为 k。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 示例 3:
#
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        len_nums=len(nums)
        if len_nums==len(set(nums)):
            return False

        for i in range(len_nums-1):
            for j in range(i+1,len_nums):
                if nums[i]==nums[j] and j-i<=k:
                    return True

        return False