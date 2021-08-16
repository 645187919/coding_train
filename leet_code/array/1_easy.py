#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-16 20:41 
# @Author : magician 
# @File : 1_easy.py 
# @Software: PyCharm


# 1. 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
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

#思路：双指针，暴力法。若时间复杂度小于O（n2）则考虑用如二分查找法
#思路二：将数组存储到词典中，然后返回对应的索引（用字典模拟哈希求解）

def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]


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

