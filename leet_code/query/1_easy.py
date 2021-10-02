#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-02 15:37 
# @Author : magician 
# @File : 1_easy.py 
# @Software: PyCharm

# 1. 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
#
#
#
# 示例 1：
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
# 示例 2：
#
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
# 示例 3：
#
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#
#
# 提示：
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# 只会存在一个有效答案

# 思路1：暴力解法
# 思路2：将元素放入map，然后查找target-一个元素的结果是否在map中。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_len=len(nums)
        if n_len==2:
            return [0,1]


        for i in range(n_len-1):
            for j in range(i+1,n_len):
                if nums[i]+nums[j]==target:
                    return [i,j]
                else:
                    continue