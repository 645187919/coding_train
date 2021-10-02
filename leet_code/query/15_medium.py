#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-08-28 17:16 
# @Author : magician 
# @File : 15.py 
# @Software: PyCharm

# 15. 三数之和
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 示例 2：
# 输入：nums = []
# 输出：[]
# 示例 3：
# 输入：nums = [0]
# 输出：[]
# 提示：（nums的大小，直接影响是否可以使用暴力法）
#
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

#思路：排序+双指针。确定一个元素，然后用双指针来遍历（双指针指向该元素后面的位置）

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        #设基础元素k,i和j分为位于k元素后的子序列中的开始和结尾的指针。
        res, k = [], 0
        #k后面还有两位所以为len-2
        for k in range(len(nums) - 2):
            #若num[k]>0,则三个正数之和大于0
            if nums[k] > 0: break
            #重复元素，则跳过，防止重复解（剪枝操作）
            if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
            #i和j分为位于k元素后的子序列中的开始和结尾的指针。
            i, j = k + 1, len(nums) - 1
            #双指针遍历子序列
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                #若s<0,则移动左边的i
                if s < 0:
                    i += 1
                    #剔除重复元素
                    while i < j and nums[i] == nums[i - 1]: i += 1
                #若s>0,则移动j
                elif s > 0:
                    j -= 1
                    #剔除重复元素
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                #s=0,添加元素组合,移动i和j。剔除i和j的重复元素
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res






