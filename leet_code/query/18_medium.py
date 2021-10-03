#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021-10-02 17:12 
# @Author : magician 
# @File : 18_medium.py 
# @Software: PyCharm

# 18. 四数之和
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] ：
#
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 你可以按 任意顺序 返回答案 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 示例 2：
#
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#
#
# 提示：
#
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

#思路：同三数之和一样。排序+双指针
#参考：https://leetcode-cn.com/problems/4sum/solution/gu-ding-liang-ge-shu-yong-shuang-zhi-zhen-zhao-lin/
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4: return []
        nums.sort()
        res = []
        for i in range(n-3):
            # 防止重复 数组进入 res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 当数组最小值和都大于target 跳出
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # 当数组最大值和都小于target,说明i这个数还是太小,遍历下一个
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            for j in range(i+1,n-2):
                # 防止重复 数组进入 res
                if j - i > 1 and nums[j] == nums[j-1]:
                    continue
                # 同理
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                # 同理
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                # 双指针
                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
        return res
